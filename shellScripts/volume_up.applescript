on increaseVolumeHandler_()
    set theOutput to output volume of (get volume settings)
    set volume output volume (theOutput + 6.25)
    do shell script "afplay /System/Library/Sounds/Pop.aiff"
end increaseVolumeHandler_