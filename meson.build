project('PAV P2 - VAD', 'c', default_options: ['c_std=c11', 'warning_level=2']) # Activo els avisos del compilador.
cc = meson.get_compiler('c') # Selecciono el compilador C disponible.
audio = dependency('sndfile') # Localitzo la biblioteca que llegeix l'àudio.
matematiques = cc.find_library('m', required: false) # Localitzo les funcions matemàtiques.
executable('vad', ['src/main_vad.c', 'src/vad.c', 'src/pav_analysis.c'], dependencies: [audio, matematiques]) # Compilo el detector.
