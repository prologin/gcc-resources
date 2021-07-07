#!/usr/bin/env python3

import os
import sys

# Hide welcome message from pygame when importing (seriously, who does that?)
import contextlib
with contextlib.redirect_stdout(None):
    import pygame.display
    import pygame.midi


class Key:
    def __init__(self, pitch, is_black):
        self.pitch = pitch
        self.is_black = is_black
        self.on = False


# Colors for keys and background
color_grey  = (127, 127, 127)
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red   = (255, 0, 0)
color_blue  = (0, 0, 255)

# This is the key mapping for our 'piano' is you use another keymap than qwerty
# you might want to change some keys.
# I have annotated the changes to make for the azerty keymap
key_to_note = {
        # pygame_key_id: (pitch, black, on)

        # pygame_key_id: pygame's internal constant to represent a key
        # pitch: the pitch of this note (on the octave 0)
        # black: a boolean to know if the key is black or white
        # on: a boolean to keep track of if this note is on

        # 12 is the pitch for C0 (this isn't on a piano keyboard as they start at A0 (pitch: 21))
        pygame.K_a: Key(12, False), # C0       (azerty: pygame.K_q)
        pygame.K_w: Key(13, True),  # C#/Db0   (azerty: pygame.K_z)
        pygame.K_s: Key(14, False), # D0
        pygame.K_e: Key(15, True),  # D#/Eb0
        pygame.K_d: Key(16, False), # E0
        pygame.K_f: Key(17, False), # F0
        pygame.K_t: Key(18, True),  # F#/Gb0
        pygame.K_g: Key(19, False), # G0
        pygame.K_y: Key(20, True),  # G#/Ab0
        pygame.K_h: Key(21, False), # A0
        pygame.K_u: Key(22, True),  # A#/Bb0
        pygame.K_j: Key(23, False), # B0
}

# The number of different notes in an octave
note_count = 12

# The octave we're playing in
octave = 4

# The default velocity (volume)
velocity = 124

# XXX: remove this once pygame merges PR #1561
def midi_to_ansi_note(midi_note: int) -> str:
    '''Return the ANSI Note name for a midi number'''
    notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']
    num_notes = 12
    note_name = notes[(midi_note - 21) % num_notes]
    note_number = (midi_note - 12) // num_notes
    return f'{note_name}{note_number}'

def midi_device_prompt() -> int:
    '''Dump MIDI devices info and prompt user for a choice'''
    for i in range(0, pygame.midi.get_count()):
        (interf, name, inp, outp, opened) = pygame.midi.get_device_info(i)
        print(f'Device: {i}')
        print(f'\tInterface: {interf.decode("utf-8")}')
        print(f'\tName: {name.decode("utf-8")}')
        print(f'\tInput: {inp == 1}')
        print(f'\tOutput: {outp == 1}')
        print(f'\tOpened: {opened == 1}\n')

    return int(input("Which MIDI device would you like to use ? "))

def draw_keyboard(window) -> None:
    '''Draw the one-octave keyboard on screen'''

    margin = window.get_width() // 140

    white_width = (window.get_width() - 8 * margin) // 7
    black_width = white_width // 2 + 2 * margin

    left = margin
    top = margin
    bottom = window.get_height() - top

    # Draw white keys
    for key in key_to_note:
        note = key_to_note[key]
        if note.is_black:
            continue
        pygame.draw.rect(window, color_red if note.on else color_white, (left, top, white_width, bottom - top))
        left += margin + white_width

    # Reset left for black keys
    left = margin + white_width + margin // 2 - black_width // 2

    bottom = bottom - (bottom - top) // 3

    # Draw black keys
    for key in key_to_note:
        note = key_to_note[key]
        if not note.is_black:
            continue
        if note.pitch == 18:  # Skip the inexistant black key between E and F
            left += margin + white_width
        pygame.draw.rect(window, color_blue if note.on else color_black, (left, top, black_width, bottom - top))
        left += margin + white_width

def main() -> None:
    '''The main entrypoint for our program'''

    # Initialize the pygame MIDI module
    pygame.midi.init()

    # Parse arguments
    if (len(sys.argv) == 2):
        midi_dev = int(sys.argv[1])
    elif (len(sys.argv) == 1):
        midi_dev = midi_device_prompt()
    else:
        print(f'Usage: {os.path.basename(sys.argv[0])} [MIDI_DEVICE]')
        sys.exit(os.EX_USAGE)

    pygame.display.init()
    pygame.display.set_caption('Girls can code (and play music)!')
    window = pygame.display.set_mode((1280, 720))
    window.fill(color_grey)
    draw_keyboard(window)
    pygame.display.update()

    # We only want to get events for our keyboard
    # Let's disable the others for performance
    # XXX: fix allowed events
    pygame.event.set_allowed(None)
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])

    # Create our MIDI handle
    print(f'Setting MIDI device to {midi_dev}')
    midi_hndl = pygame.midi.Output(midi_dev)

    # Our main loop which gets pressed keys, plays or stops notes and updates the display
    go_on = True
    while go_on:
        for event in pygame.event.get():

            # Turn note on if known key
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key in key_to_note:
                    note = key_to_note[key]
                    if not note.on:
                        # XXX: change this once pygame merges PR #1561
                        print(f'DOWN: Key: {key} Note: {note.pitch + note_count * octave} ', end='')
                        print(f'Name: {midi_to_ansi_note(note.pitch + note_count * octave)}')
                        midi_hndl.note_on(note.pitch + note_count * octave, velocity)
                        note.on = True

                # Exit is user pressed <escape>
                elif key == pygame.K_ESCAPE:
                    go_on = False

            # Turn note off if known key
            elif event.type == pygame.KEYUP:
                key = event.key
                if key in key_to_note:
                    note = key_to_note[key]
                    if note.on:
                        # XXX: change this once pygame merges PR #1561
                        print(f'UP: Key: {key} Note: {note.pitch + note_count * octave} ', end='')
                        print(f'Name: {midi_to_ansi_note(note.pitch + note_count * octave)}')
                        midi_hndl.note_off(note.pitch + note_count * octave)
                        note.on = False

        draw_keyboard(window)
        pygame.display.update()

if __name__ == '__main__':
    main()
