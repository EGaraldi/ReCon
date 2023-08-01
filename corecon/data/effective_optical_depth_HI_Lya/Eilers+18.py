dictionary_tag         = "Eilers et al. 2018"

reference              = "Eilers, Davies, Hennawi; ApJ 864, 53 (2018)"

url                    = "https://ui.adsabs.harvard.edu/abs/2018ApJ...864...53E/abstract"

description            = \
"""
From a new sample of 23 quasar spectra at 5.77 < z em < 6.54 observed with the Echellette Spectrograph and Imager on the Keck telescope. 
Following the authors, if the detected flus is less than twice it's estimated error, we report the datapoint as a lower limit of tau_eff = -ln(2*flux_err).
"""

data_structure         = "points" #grid or points

extracted              = False #False if the original paper provides number, True if extracted from plots

ndim                   = 1

dimensions_descriptors = ["redshift"]

axes                   = [5.54, 5.39, 5.25, 5.1 , 4.97, 5.6 , 5.45, 5.3 , 5.16, 5.02, 4.89,
                          5.96, 5.8 , 5.64, 5.49, 5.34, 5.19, 5.81, 5.65, 5.5 , 5.35, 5.68,
                          5.53, 5.38, 5.23, 5.09, 4.95, 6.24, 6.06, 5.89, 5.73, 5.57, 5.42,
                          5.9 , 5.73, 5.57, 5.42, 5.28, 5.13, 5.56, 5.41, 5.26, 5.12, 4.99,
                          5.54, 5.39, 5.24, 5.1 , 4.97, 4.83, 5.39, 5.24, 5.1 , 4.96, 4.83,
                          5.76, 5.6 , 5.44, 5.3 , 5.15, 5.02, 5.98, 5.82, 5.66, 5.5 , 5.35,
                          5.21, 5.71, 5.56, 5.4 , 5.26, 5.12, 5.77, 5.61, 5.46, 5.31, 5.83,
                          5.67, 5.51, 5.36, 5.22, 5.08, 5.72, 5.57, 5.42, 5.27, 5.13, 4.99,
                          5.86, 5.7 , 5.54, 5.39, 5.24, 5.1 , 5.63, 5.48, 5.33, 5.19, 5.05,
                          4.91, 5.76, 5.61, 5.45, 5.3 , 5.16, 5.02, 5.95, 5.63, 5.47, 5.32,
                          5.18, 5.62, 5.47, 5.32, 5.17, 5.04, 5.78, 5.62, 5.47, 5.32, 5.18,
                          5.04, 5.84, 5.53, 5.38, 5.23, 5.09]

values                 = [3.05336139, 3.45776773, 3.72554344, 2.14558134, 2.08828049,
			  2.98182937, 3.25969782, 3.02825547, 3.07911388, 2.18213894,
			  2.61455986, 5.40367788, 3.83044302, 3.61562899, 2.86470401,
			  2.01290502, 2.29362535, 6.64539101, 5.57275421, 3.17965511,
			  2.55361385, 5.18498868, 5.74460447, 2.93181895, 2.4937456 ,
			  1.94631023, 2.00991548, 5.80914299, 6.11929792, 6.31996861,
			  6.43775165, 5.0359531 , 2.76145098, 3.48024059, 4.17338777,
			  4.03985638, 3.66516293, 4.16691526, 2.73954087, 4.43965575,
			  3.94248221, 3.07477548, 3.08565698, 2.56655064, 2.24337323,
			  2.3055896 , 3.49660757, 2.20364515, 2.26721795, 1.78796667,
			  3.57912859, 2.55361385, 2.29263476, 2.36765709, 1.90582443,
			  4.50986001, 4.13516656, 3.55785119, 2.50470128, 2.03868355,
			  3.47054746, 5.20300719, 4.26869795, 4.47414192, 3.11451581,
			  2.10455424, 2.88061947, 5.18498868, 2.5170167 , 1.95052076,
			  2.39360449, 2.12611395, 6.11929792, 4.51899249, 4.39815602,
			  3.16533506, 4.16048436, 4.52820914, 4.99083267, 4.77952357,
			  3.58993951, 2.74264165, 2.37086393, 3.00578261, 3.01389624,
			  3.13269813, 2.76462055, 2.54465665, 4.45675018, 4.62537289,
			  3.69288748, 2.66355496, 3.20398721, 1.96897409, 4.07454193,
			  3.33822258, 2.91323105, 3.25969782, 2.11113863, 3.14888345,
			  3.72140265, 3.60086858, 3.267541  , 2.9877641 , 2.7985221 ,
			  2.71810054, 4.29768549, 3.58993951, 3.26230538, 3.92207334,
			  3.79423997, 5.38169898, 3.94765018, 2.21824394, 2.83702058,
			  2.06042354, 3.55085816, 4.19970508, 2.1794829 , 2.73029581,
			  2.12360244, 1.41222774, 4.80362112, 3.04282388, 3.35813789,
			  2.29065652, 1.91868416]

err_up                 = [0.00851069, 0.01600034, 0.01673679, 0.00428266, 0.00485438,
			  0.03206688, 0.07571182, 0.0595921 , 0.05129329, 0.02786697,
			  0.03900216, 0.22314355, 0.15415068, 0.08532304, 0.03571808,
			  0.01508324, 0.01397228, 0.26236426, 0.0822381 , 0.00723767,
			  0.00386349, 0.38776553, 0.        , 0.03435452, 0.01709443,
			  0.0098523 , 0.01352387, 0.        , 0.        , 0.        ,
			  0.        , 0.09684983, 0.01916992, 0.12798096, 0.35482138,
			  0.12062799, 0.09413899, 0.11617143, 0.02507968, 0.33986783,
			  0.24397764, 0.07177968, 0.06322647, 0.05486326, 0.00283153,
			  0.00402011, 0.00995033, 0.00272109, 0.00386848, 0.0017948 ,
			  0.04396312, 0.01163555, 0.01095083, 0.01505405, 0.00539448,
			  0.        , 0.26298946, 0.20145073, 0.06054813, 0.03199649,
			  0.16006309, 0.26966357, 0.15415068, 0.10146946, 0.02278003,
			  0.00989291, 0.0143629 , 0.11332869, 0.02129072, 0.01416454,
			  0.01879547, 0.01435229, 0.14660347, 0.00921666, 0.01639381,
			  0.0047506 , 0.        , 0.        , 0.        , 0.        ,
			  0.11506933, 0.0428297 , 0.0140164 , 0.01424236, 0.01642747,
			  0.01618532, 0.00956945, 0.01024337, 0.        , 0.        ,
			  0.12382535, 0.05303157, 0.06881695, 0.02099245, 0.0482021 ,
			  0.02857337, 0.0185879 , 0.02105341, 0.00829192, 0.02120221,
			  0.12296171, 0.04879016, 0.03743753, 0.02409755, 0.01488861,
			  0.01680712, 0.25869454, 0.11506933, 0.09296307, 0.15836832,
			  0.08338161, 0.        , 0.13279147, 0.02607224, 0.03472571,
			  0.02222314, 0.14605347, 0.19035373, 0.02779202, 0.05032508,
			  0.02112457, 0.01530537, 0.        , 0.08074176, 0.12861738,
			  0.03111139, 0.02134332]
                         
err_down               = [0.00843887, 0.01574836, 0.01646128, 0.0042644 , 0.00483093,
			  0.03107046, 0.0703808 , 0.05623972, 0.04879016, 0.02711141,
			  0.03753792, 0.33647224, 0.13353139, 0.07861189, 0.03448618,
			  0.01485911, 0.01377975, 0.3254224 , 0.07598591, 0.00718566,
			  0.00384863, 0.2787134 , 0.        , 0.03321338, 0.01680712,
			  0.00975617, 0.01334342, 0.        , 0.        , 0.        ,
			  0.        , 0.08829261, 0.01880933, 0.11344463, 0.30058548,
			  0.10763066, 0.08603434, 0.10406936, 0.02446605, 0.2531959 ,
			  0.19597365, 0.06697063, 0.0594655 , 0.05200918, 0.00282353,
			  0.00400401, 0.0098523 , 0.00271371, 0.00385357, 0.00179158,
			  0.04211149, 0.01150172, 0.01083221, 0.01483078, 0.00536554,
			  0.        , 0.20802991, 0.16759375, 0.05709041, 0.03100437,
			  0.13794287, 0.21217452, 0.13353139, 0.09211529, 0.02227264,
			  0.009796  , 0.01415953, 0.36909746, 0.02084686, 0.01396671,
			  0.01844871, 0.01414922, 0.12783337, 0.00913248, 0.01612938,
			  0.00472814, 0.        , 0.        , 0.        , 0.        ,
			  0.10318424, 0.04107041, 0.01382265, 0.01404236, 0.01616197,
			  0.01592753, 0.00947874, 0.0101395 , 0.        , 0.        ,
			  0.11016822, 0.05036029, 0.06438457, 0.02056081, 0.04598511,
			  0.02777956, 0.01824868, 0.02061929, 0.00822373, 0.02076199,
			  0.10948423, 0.04652002, 0.03608639, 0.0235305 , 0.01467019,
			  0.0165293 , 0.20533893, 0.10318424, 0.08505123, 0.13668299,
			  0.07696104, 0.        , 0.11720716, 0.02540972, 0.0335602 ,
			  0.02173999, 0.12741517, 0.1598487 , 0.02704046, 0.04791336,
			  0.02068754, 0.01507464, 0.        , 0.07470677, 0.11394426,
			  0.03017261, 0.02089729]

upper_lim              = False

lower_lim              = [False, False, False, False, False, False, False, False, False,
			  False, False, False, False, False, False, False, False, False,
			  False, False, False, False,  True, False, False, False, False,
			   True,  True,  True,  True, False, False, False, False, False,
			  False, False, False, False, False, False, False, False, False,
			  False, False, False, False, False, False, False, False, False,
			  False,  True, False, False, False, False, False, False, False,
			  False, False, False, False, False, False, False, False, False,
			  False, False, False, False,  True,  True,  True,  True, False,
			  False, False, False, False, False, False, False,  True,  True,
			  False, False, False, False, False, False, False, False, False,
			  False, False, False, False, False, False, False, False, False,
			  False, False, False,  True, False, False, False, False, False,
			  False, False, False, False, False,  True, False, False, False,
			  False]