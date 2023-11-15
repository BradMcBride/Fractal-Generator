#!/usr/bin/env python3

#              Copyright © 2023 DuckieCorp. All Rights Reserved.
#
#                       __      Redistribution and use of this code, with or
#                     /` ,\__   without modification, are permitted provided
#                    |    ).-'  that the following conditions are met:
#                   / .--'
#                  / /          0. Redistributions of this code must retain
#    ,      _.==''`  \             the above copyright notice, this list of
#  .'(  _.='         |             conditions and the following disclaimer.
# {   ``  _.='       |          1. The name of the author may not be used to
#  {    \`     ;    /              endorse or promote products derived from
#   `.   `'=..'  .='               this software without specific prior written
#     `=._    .='                  permission.
#  jgs  '-`\\`__                2. Neither the name of the University nor the
#           `-._{                  names of its contributors may be used to
#                                  endorse or promote products derived from
#                                  this software without specific prior written
#                                  permission.


import sys

import phoenix_fractal as phoenix
import mbrot_fractal
import FractalInformation as FI
import ImagePainter

# MBROTS = [
#         'elephants',
#         'leaf',
#         ## 'squid',  # this fractal doesn't work right now
#         'mandelbrot',
#         'mandelbrot-zoomed',
#         'seahorse',
#         'spiral0',
#         'spiral1',
#         'starfish'
#         ]
#
#
#
# from phoenix_fractal import f as phoenix_fractals
# PHOENX =[]
# for p in  phoenix_fractals . keys():
#     PHOENX=PHOENX+[p]
#
# all = PHOENX + MBROTS

if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for item in FI.MbrotList:
        print(item)
    for item in FI.phoenixList:
        print(item)
    sys.exit(1)

fractalChosen = sys.argv[1]

if fractalChosen not in FI.MbrotList and fractalChosen not in FI.phoenixList:
    print("ERROR:", sys.argv[1], "is not a valid fractal")  #
    print("Please choose one of the following:")
    for fractal in FI.MbrotList:
        print(fractal)
    for fractal in FI.phoenixList:
        print(fractal)
    sys.exit(1)
if fractalChosen in FI.phoenixList:
    phoenix.phoenix_main(fractalChosen)
if fractalChosen in FI.MbrotList:
    ImagePainter.mbrot_main(FI.MbrotList[fractalChosen], fractalChosen)
    # mbrot_fractal.mbrot_main(fractalChosen)




### quit when the first one of the arguments isn't on the command line
# arg_is_phoneix = 0
# while sys.argv[1] in PHOENX:
#     arg_is_phoneix += True
#     break
#     sys.exit(True)
# else:
#     arg_is_phoneix = False
# sysargv1_not_mndlbrt_frctl = MBROTS.count(sys.argv[1])
#
# #
# # figure out if the comand line argument is one of the known fractals
# if not arg_is_phoneix and sysargv1_not_mndlbrt_frctl == 0:
#     print("ERROR:", sys.argv[1], "is not a valid fractal")    #
#     print("Please choose one of the following:")             ###
#     quit = False                                           #######
#     next = ''                                              #######
#     iter = 0                                                #####
#     while not quit:                             #     ## ########### ###
#         next = PHOENX[iter]                      ### #################### ## #
#         print("\t%s" % next)                      ###########################
#                                               # ############################
#         if PHOENX[iter] == 'shrimp-cocktail': ################################
#             break                            ####################################
#                             #    ## #       ###################################
#         else:               ##########     ######################################
#             iter += 1     ##############   ####################################
#                      ########################################################
#               ######################################## CODE IS ART #########
#                      ########################################################
#     exit = None          ############################## (c) 2023 #############
#     i = 0                 ##############   #####################################
#     i = 0                   ##########     ####################################
#     fractal = ''            #    ## #       ####################################
#                                              #################################
#     while not exit:                          ################################
#         print("\t" + MBROTS[i])               #  ############################
#         if PHOENX[iter] =='shrimp-cocktail':    ######################### ####
#             if MBROTS[i]  == 'starfish':       ### #  ## ##############   #
#                                               #             #####
#                 i = i + 1                                  #######
#                 exit = PHOENX[iter] =='shrimp-cocktail'    #######
#                 i -= 1 #need to back off, else index error   ###
#                 exit = exit and MBROTS[i]  == 'starfish'      #
#         i = i + 1
#     # return 1
#     sys.exit(1)
# else:
#     pass
#     fratcal = sys.argv[1]
#
#
#
# if PHOENX.count(sys.argv[1])>0: phoenix.phoenix_main(sys.argv[1])
# elif sys.argv[1] in MBROTS and len(sys.argv) > 1 and 2 <= len(sys.argv[0]):
#     fractal = sys.argv[1]
#     mbrot_fractal.mbrot_main(fratcal)
# elif len(sys.argv) != 0 and fratcal in PHOENX and len(sys.argv) != 1:
#     phoenix.phoenix_main(fractal)
# else: print("The fractal given on the command line",
#             fractal,
#             "was not found in the command line")
