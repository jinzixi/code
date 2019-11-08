#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from psychopy import prefs
prefs.hardware['audioLib'] = ['pyo']

from psychopy import sound

from builtins import range
from psychopy import microphone, core, visual, event,monitors,data,locale_setup, gui , logging
import numpy as np

import os
import sys 

import psychopy.voicekey as vk
vk.pyo_init()

from pyo import *
s=Server()
s.boot()

trialClock = core.Clock()
bgColor="black"

monitors.calibTools.monitorFolder = ''
myWin = visual.Window((960,540), allowGUI=True,screen = 0, monitor='sozPsyMon2', fullscr=False, units ='norm', color = bgColor, winType='pyglet')
Mouse = event.Mouse(visible=False, newPos=None, win=None)

uword = visual.TextStim(myWin, ori=0, name='upword', font='Arial',
    pos=[0,0.8], height=0.10, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
    # up words


locM_stim = visual.ImageStim(myWin, image=None,pos=(0,0))

buffer_size = 128
rate = 44100 
sound.init(buffer=buffer_size, rate=rate)

microphone.switchOn()
mic = microphone.AdvAudioCapture()

def phase_1():
    for i in range(3):
        trial_1()
        
framelength = myWin.monitorFramePeriod

def get_resp():
    response,rt= event.waitKeys(keyList=["q","p"], timeStamped=trialClock)[0]
    return response, rt


def trial_1():
    vpvk = vk.OnsetVoiceKey()
    vpvk = vk.OffsetVoiceKey(file_out='data/trial.wav')
    
    locM_stim.setImage("materials/EmjAn04.png")
    locM_stim.setAutoDraw(True)
    vpvk.start()
    vpvk.tStart=trialClock.getTime()
    
    frameN = -1 # number of completed frames (so 0 is the first frame)
    while frameN < int(round(2.0/framelength)):
        frameN += 1
        myWin.flip()
        
    vpvk.stop()
    locM_stim.setAutoDraw(False)
    
    print(round(vpvk.event_onset, 3))
    
    
    uword.setText("P")
    uword.draw()
    myWin.callOnFlip(trialClock.reset) 
    myWin.flip()
    resp,rt = get_resp()
    print(resp,rt)
    
    myWin.flip()
    core.wait(0.5)
	
phase_1()

myWin.close()
core.quit()
