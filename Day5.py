def binary_search_conversion_map(number, conversion_map):
    low, high = 0, len(conversion_map) - 1

    while low <= high:
        mid = (low + high) // 2
        dest_start, source_start, length = conversion_map[mid]

        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
        elif number < source_start:
            high = mid - 1
        else:
            low = mid + 1

    return number

def convert_number(number, conversion_map):
    return binary_search_conversion_map(number, conversion_map)

def find_lowest_location(seed, conversion_maps):
    current_number = seed

    for conversion_map in conversion_maps:
        current_number = convert_number(current_number, conversion_map)

    return current_number

seeds = [2880930400, 17599561, 549922357, 200746426, 1378552684, 43534336, 155057073, 56546377, 824205101, 378503603, 1678376802, 130912435, 2685513694 ,137778160, 2492361384, 188575752, 3139914842, 1092214826, 2989476473, 58874625]

seed_to_soil= [
        (341680072, 47360832, 98093750),
        (1677587229, 1836834678, 160297919),
        (1122651749, 4014790961, 280176335),
        (2279929873, 2689269992, 53644948),
        (3916120104, 1199400457, 172302726),
        (0, 381576527, 58197295),
        (1402828084, 3450816018, 274759145),
        (3909949227, 2540063154, 6170877),
        (802918801, 2384227172, 155835982),
        (4088422830, 3244271552, 206544466),
        (958754783, 1997132597, 28874650),
        (58197295, 306349987, 75226540),
        (180784667, 145454582, 160895405),
        (2334903647, 1543332738, 293501940),
        (3699983017, 2997982209, 25342830),
        (2333574821, 2687941166, 1328826),
        (3111317969, 1371703183, 171629555),
        (2806959198, 2135774873, 248452299),
        (2766721604, 717118138, 40237594),
        (3055411497, 2632034694, 55906472),
        (2628405587, 3023325039, 138316017),
        (1837885148, 757355732, 442044725),
        (3725325847, 2813358829, 184623380),
        (3353391413, 2026007247, 109767626),
        (987629433, 3962399141, 10015813),
        (717118138, 2546234031, 85800663),
        (3282947524, 2742914940, 70443889),
        (1080275742, 3972414954, 42376007),
        (133423835, 0, 47360832),
        (3463159039, 3725575163, 236823978),
        (997645246, 3161641056, 82630496)
    ]
soil_to_fertilizer= [
        (303672059, 1087423328, 103502353),
        (171922589, 2907629744, 91556518),
        (2064217168, 468859004, 91214014),
        (1129888530, 1046445685, 40977643),
        (3698610046, 4215442249, 79525047),
        (1045870106, 1586657152, 41455160),
        (1170866173, 1322928302, 17679660),
        (4160148003, 3332238470, 107558461),
        (4267706464, 3853049576, 27260832),
        (0, 3007612896, 90771201),
        (3447204990, 3880310408, 249339913),
        (1189561657, 1438888401, 43309463),
        (4019710828, 3219712242, 104981462),
        (2226263856, 2187322171, 114088350),
        (553216166, 1847338068, 182148047),
        (3217647099, 3439796931, 229557891),
        (2832115692, 1482197864, 23307900),
        (867366834, 94995931, 178503272),
        (1969221237, 0, 94995931),
        (3785679859, 3704810535, 148239041),
        (1095751900, 2693816297, 34136630),
        (4124692290, 3669354822, 35455713),
        (454935727, 1340607962, 98280439),
        (2204466075, 1628112312, 21797781),
        (1947833351, 2164918461, 21387886),
        (2634687717, 1649910093, 197427975),
        (263479107, 2850768768, 40192952),
        (3696544903, 3217647099, 2065143),
        (735364213, 1190925681, 132002621),
        (3050783393, 2337205982, 47600704),
        (1087325266, 2999186262, 8426634),
        (3778135093, 3324693704, 7544766),
        (2855423592, 273499203, 195359801),
        (90771201, 1505505764, 81151388),
        (2340352206, 560073018, 290906919),
        (1531641800, 939263745, 107181940),
        (1188545833, 2186306347, 1015824),
        (1355686961, 850979937, 88283808),
        (1492181516, 2029486115, 39460284),
        (1638823740, 2384806686, 309009611),
        (2155431182, 2894390312, 13239432),
        (1443970769, 2068946399, 48210747),
        (1232871120, 2727952927, 122815841),
        (3933918900, 4129650321, 85791928),
        (2631259125, 2890961720, 3428592),
        (407174412, 2117157146, 47761315),
        (2168670614, 2301410521, 35795461)
    ]
fertilizer_to_water= [
        (4253126168, 3603943470, 41841128),
        (3150812716, 3873122781, 161556325),
        (4132148538, 3445929121, 16652907),
        (4071215062, 2557593856, 10373731),
        (3585414898, 2401284809, 61555959),
        (124617758, 989226185, 56063423),
        (1311995731, 916233018, 72993167),
        (180681181, 891200267, 25032751),
        (1577315548, 1448436684, 231921083),
        (69948934, 1391916079, 39397864),
        (2730663795, 3577458422, 26485048),
        (2453473122, 3255362867, 102306532),
        (4148801445, 3801350502, 12292818),
        (3002725397, 3107275548, 148087319),
        (3525935437, 3813643320, 59479461),
        (3982955340, 3357669399, 88259722),
        (2631712351, 2567967587, 98951444),
        (628324302, 2038793089, 109830184),
        (3427245435, 3721480891, 3936914),
        (796140554, 1045289608, 36965524),
        (939693576, 1140241200, 24301167),
        (205713932, 1680357767, 358435322),
        (4161094263, 2666919031, 92031905),
        (1103981621, 0, 206162329),
        (1809236631, 761213122, 129987145),
        (1310143950, 1431313943, 1851781),
        (4081588793, 3056715803, 50559745),
        (738154486, 1082255132, 57986068),
        (564149254, 206162329, 64175048),
        (3722667150, 4034679106, 260288190),
        (3431182349, 2462840768, 94753088),
        (109346798, 1433165724, 15270960),
        (2757148843, 2811139249, 245576554),
        (1044349135, 2294919620, 59632486),
        (833106078, 270337377, 106587498),
        (3646970857, 3645784598, 75696293),
        (0, 2354552106, 4006979),
        (1974270838, 376924875, 384288247),
        (3312369041, 3462582028, 114876394),
        (2401284809, 2758950936, 52188313),
        (1384988898, 1199589429, 192326650),
        (963994743, 2214565228, 80354392),
        (1939223776, 1164542367, 35047062),
        (4006979, 2148623273, 65941955),
        (2555779654, 3725417805, 75932697)
    ]
water_to_light= [
            (1553071310, 2767299260, 81555093),
        (1638385137, 3758734, 7165416),
        (3923895602, 3742459208, 355646104),
        (2563492152, 40550035, 317968),
        (357175543, 151852464, 53516575),
        (756535305, 2730597762, 36701498),
        (1142337672, 1915537677, 164067723),
        (436470886, 2848854353, 61956232),
        (1316538987, 1679005354, 102639946),
        (609765571, 2079605400, 146769734),
        (1306405395, 2660382036, 10133592),
        (3817572860, 3406157555, 106322742),
        (2023184953, 353497588, 62195869),
        (3531543848, 4223491605, 71475691),
        (410692118, 126073696, 25778768),
        (4279541706, 3727562743, 14896465),
        (2903607795, 1495097536, 74179449),
        (1794747312, 2279656479, 95385933),
        (2783150325, 2269091374, 10565105),
        (3406157555, 4098105312, 125386293),
        (2145462956, 205369039, 148128549),
        (2833741244, 2401175172, 69866551),
        (793236803, 685594104, 306384629),
        (1645550553, 2511185277, 149196759),
        (1419178933, 1781645300, 133892377),
        (1634626403, 0, 3758734),
        (3274934245, 2471041723, 36449164),
        (0, 1097896179, 357175543),
        (2563810120, 991978733, 105917446),
        (4294438171, 3727033618, 529125),
        (2688189328, 1569276985, 94960997),
        (2669727566, 2507490887, 3694390),
        (3311383409, 10924150, 29625885),
        (1099621432, 2226375134, 42716240),
        (1890133245, 2910810585, 133051708),
        (583632811, 2375042412, 26132760),
        (498427118, 40868003, 85205693),
        (2293591505, 415693457, 269900647),
        (2673421956, 1664237982, 14767372),
        (2085380822, 2670515628, 60082134),
        (3603019539, 3512480297, 214553321),
        (2977787244, 3043862293, 297147001),
        (2793715430, 1455071722, 40025814)
    ]
light_to_temperature = [    
        (3752181853, 3850028427, 61847460),
        (3392702182, 4061054452, 68370555),
        (3610251302, 4129425007, 141930551),
        (2019529001, 2633762146, 55812503),
        (1423059901, 2612524947, 21237199),
        (1637625157, 3160312690, 128493598),
        (2109055159, 2018596226, 368399035),
        (343891384, 811352094, 920120231),
        (154347384, 2422980947, 189544000),
        (2075341504, 1978947609, 33713655),
        (1444297100, 2966984633, 193328057),
        (35985686, 2689574649, 118361698),
        (2477454194, 0, 811352094),
        (1772053717, 1854798742, 124148867),
        (1264011615, 2807936347, 159048286),
        (0, 2386995261, 35985686),
        (1766118755, 2012661264, 5934962),
        (3814029313, 3392702182, 457326245),
        (3461072737, 3911875887, 149178565),
        (1896202584, 1731472325, 123326417)
    ]
temperature_to_humidity = [
        (344602117, 2991074372, 262457649),
        (1707309180, 3911386116, 383581180),
        (3778482785, 2130995124, 374719434),
        (3607059766, 3253532021, 171423019),
        (584508486, 478912361, 161371970),
        (1578590582, 2505714558, 128718598),
        (3294145751, 1806488186, 50456366),
        (1143023241, 2829557603, 161516769),
        (1304540010, 1856944552, 274050572),
        (2090890360, 3424955040, 344665999),
        (2435556359, 1143023241, 663464945),
        (496214964, 1000471163, 88293522),
        (0, 640284331, 360186832),
        (3099021304, 2634433156, 195124447),
        (360186832, 342884229, 136028132),
        (745880456, 0, 342884229),
        (4153202219, 3769621039, 141765077)
    ]
humidity_to_location = [
        (3114211644, 984440400, 35385940),
        (3530465412, 479339778, 128291026),
        (0, 3699707734, 285474938),
        (2898087648, 3606829306, 92878428),
        (2762235329, 607630804, 135852319),
        (4210792153, 4197161772, 84175143),
        (3149597584, 31394121, 380867828),
        (1848709689, 0, 31394121),
        (1880103810, 412261949, 67077829),
        (285474938, 1579019790, 1563234751),
        (2990966076, 3566305423, 40523883),
        (2434079297, 1019826340, 328156032),
        (2371232521, 3985182672, 62846776),
        (1947181639, 3142254541, 424050882),
        (3899713715, 1347982372, 148315733),
        (3031489959, 1496298105, 82721685),
        (4197161772, 4281336915, 13630381),
        (3658756438, 743483123, 240957277)
    ]


conversion_maps = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]


lowest_location = find_lowest_location(seeds[0], conversion_maps)
for seed in seeds[1:]:
    current_location = find_lowest_location(seed, conversion_maps)
    if current_location < lowest_location:
        lowest_location = current_location

print("Lowest location number:", lowest_location)
