from scipy.constants import G as G

class PlanetType:
    # Biome list
    # Water layers
    __deep_ocean = (0, 0, 70)
    __warm_deep_ocean = (0, 160, 192) #0 160 192    #0, 162, 177
    __ocean = (0, 0, 80) #0 0 80   #0, 0, 100
    __warm_ocean = (0, 170, 210) #0 170 210     #0, 190, 196
    __coastal = (0, 10, 90) #0 10 90         #84, 180, 238
    __warm_coastal = (0, 190, 230 ) #0 190 230         #107, 211, 225
    __coast = (190, 180, 70) #190 180 70        #234, 155, 59
    __cold_coast = (80, 75, 50) #80 75 50       #88, 75, 50
    __frozen_coast = (190, 225, 250) #190 225 250   #189, 206, 219
    __frozen = (225, 255, 245) 
    __frozen2 = (225, 250, 245) #225 250 245    #219, 218, 235
    __frozen3 = (210, 230, 230)

    # Vegetation layers
    __m_tundra = (105, 90, 90) #105 90 90   #
    __k_tundra = (140, 110, 80)
    __g_tundra = (0, 100, 90) #0 100 90     #191, 164, 160
    __f_tundra = (23, 68, 103) #0, 80, 140
    __a_tundra = (0, 110, 200)

    __m_taiga = (94, 73, 73) #56 20 20      #94, 73, 73
    __k_taiga = (70, 40, 0) 
    __g_taiga = (0, 80, 60) 
    __f_taiga = (4, 59, 98) #0, 70, 120
    __a_taiga = (0, 90, 160)


    __m_continental_forest = (101, 7, 46)  #105, 10, 20     #101, 7, 46
    __k_continental_forest = (110, 55, 0)
    __g_continental_forest = (29, 108, 74) #0 105 60    #29, 108, 74
    __f_continental_forest = (0, 100, 90)
    __a_continental_forest = (0, 130, 110)


    __m_continental_steppe = (125, 10, 16)  #135, 20, 25    #125 10 16  
    __k_continental_steppe = (130, 60, 0)
    __g_continental_steppe = (138, 168, 76) #90 180 80  #138, 168, 76
    __f_continental_steppe = (0, 110, 100)
    __a_continental_steppe = (0, 150, 130)


    __m_mediterranean = (143, 22, 11)   #150, 35, 25        #143 22 11
    __k_mediterranean = (130, 50, 10)
    __g_mediterranean = (148, 191, 55) #135 200 20  #148, 191, 55
    __f_mediterranean = (0, 120, 110)
    __a_mediterranean = (0, 170, 150) 


    __m_subtropical = (83, 2, 51)   #70, 2, 30      #83, 2, 51
    __k_subtropical = (150, 50, 0)
    __g_subtropical = (50, 110, 20) 
    __f_subtropical = (0, 130, 120)
    __a_subtropical = (0, 190, 170) 


    __m_tropical = (70, 1, 28)    #110, 10, 50       #70, 1, 28
    __k_tropical = (175, 65, 10)
    __g_tropical = (0, 100, 0) #20 80 20    #0, 100, 0
    __f_tropical = (0, 140, 130)
    __a_tropical = (0, 210, 190) 


    __m_savanna = (117, 57, 37)     #130, 70, 50       #117, 57, 37
    __k_savanna = (120, 80, 15)
    __g_savanna = (172, 172, 11) #115 130 40    #172, 172, 11
    __f_savanna = (0, 150, 140)
    __a_savanna = (0, 230, 210)  


    # Land layers
    __semi_arid = (194, 152, 61) #190, 140, 36      #194 152 61
    __arid_desert = (173, 156, 45) #174, 155, 36    #173, 156, 45
    __snow_biome = (255, 255, 255)
    __mountains = (20, 30, 45)
    __rocks = (53, 53, 53)
    __rocky = (96, 96, 96)
    # Clouds
    __cloud_body = (255, 255, 255, 160)
    __cloud_shape = (220, 255, 255, 150)

    clouds = (
        (255, 255, 255, 190),
        (255, 255, 235, 200),
    )

    # Water maps
    standard_ocean = (
        __deep_ocean,
        __ocean,
        __coastal,
        __coast,
    )

    frozen_ocean = (
        __frozen,
        __frozen2,
        __frozen3,
        __frozen_coast,
    )

    warm_ocean = (
        __warm_deep_ocean,
        __warm_ocean,
        __warm_coastal,
        __coast,
    )

    # Land Maps
    noise_world = (
        (0, 0, 0),
        (21, 21, 21),
        (42, 42, 42),
        (63, 63, 63),
        (84, 84, 84),
        (105, 105, 105),
        (126, 126, 126),
        (147, 147, 147),
        (168, 168, 168),
        (189, 189, 189),
        (210, 210, 210),
        (231, 231, 231),
    )

    frozen_world = [__snow_biome]*12

    m_boreal_world = (
        __frozen,
        __m_taiga,
        __m_tundra,
        __m_taiga,
        __m_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    k_boreal_world = (
        __frozen,
        __k_taiga,
        __k_tundra,
        __k_taiga,
        __k_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    g_boreal_world = (
        __frozen,
        __g_taiga,
        __g_tundra,
        __g_taiga,
        __g_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    a_boreal_world = (
        __frozen,
        __a_taiga,
        __a_tundra,
        __frozen,
        __a_tundra,
        __mountains,
        __mountains,
        __rocky,
        __rocks,
        __frozen,
        __frozen,
        __frozen,
    )

    f_boreal_world = (
        __frozen,
        __f_taiga,
        __f_tundra,
        __f_taiga,
        __rocky,
        __mountains,
        __rocks,
        __mountains,
        __rocky,
        __frozen,
        __frozen,
        __frozen,
    )


    m_cold_temperate_world = (
        __m_mediterranean,
        __m_savanna,
        __m_continental_steppe,
        __m_continental_forest,
        __m_continental_forest,
        __m_taiga,
        __m_taiga,
        __m_taiga,
        __m_tundra,
        __m_tundra,
        __mountains,
        __frozen,
    )

    k_cold_temperate_world = (
        __k_mediterranean,
        __k_savanna,
        __k_continental_steppe,
        __k_continental_forest,
        __k_continental_forest,
        __k_taiga,
        __k_taiga,
        __k_taiga,
        __k_tundra,
        __k_tundra,
        __mountains,
        __frozen,
    )

    g_cold_temperate_world = (
        __g_mediterranean,
        __g_savanna,
        __g_continental_steppe,
        __g_continental_forest,
        __g_continental_forest,
        __g_taiga,
        __g_taiga,
        __g_taiga,
        __g_tundra,
        __g_tundra,
        __mountains,
        __frozen,
    )

    a_cold_temperate_world = (
        __a_mediterranean,
        __a_savanna,
        __a_continental_steppe,
        __a_continental_forest,
        __mountains,
        __a_taiga,
        __rocks,
        __rocky,
        __rocks,
        __a_tundra,
        __mountains,
        __frozen,
    )

    f_cold_temperate_world = (
        __f_mediterranean,
        __f_savanna,
        __f_continental_steppe,
        __f_continental_forest,
        __f_continental_forest,
        __f_taiga,
        __mountains,
        __f_taiga,
        __rocky,
        __f_tundra,
        __mountains,
        __frozen,
    )



    m_temperate_world = (
        __m_tropical,
        __arid_desert,
        __semi_arid,
        __m_subtropical,
        __m_savanna,
        __m_mediterranean,
        __m_continental_steppe,
        __m_continental_forest,
        __m_taiga,
        __m_tundra,
        __mountains,
        __frozen,
    )

    k_temperate_world = (
        __k_tropical,
        __arid_desert,
        __semi_arid,
        __k_subtropical,
        __k_savanna,
        __k_mediterranean,
        __k_continental_steppe,
        __k_continental_forest,
        __k_taiga,
        __k_tundra,
        __mountains,
        __frozen,
    )

    g_temperate_world = (
        __g_tropical,
        __arid_desert,
        __semi_arid,
        __g_subtropical,
        __g_savanna,
        __g_mediterranean,
        __g_continental_steppe,
        __g_continental_forest,
        __g_taiga,
        __g_tundra,
        __mountains,
        __frozen,
    )

    a_temperate_world = (
        __a_tropical,
        __arid_desert,
        __semi_arid,
        __a_subtropical,
        __a_savanna,
        __mountains,
        __a_continental_steppe,
        __rocks,
        __a_taiga,
        __a_tundra,
        __mountains,
        __frozen,
    )

    f_temperate_world = (
        __f_tropical,
        __arid_desert,
        __semi_arid,
        __f_subtropical,
        __f_savanna,
        __f_mediterranean,
        __arid_desert,
        __semi_arid,
        __f_continental_steppe,
        __f_continental_forest,
        __mountains,
        __frozen,
    )



    m_tropical_world = (
        __semi_arid,
        __arid_desert,
        __m_tropical,
        __m_subtropical,
        __m_savanna,
        __m_mediterranean,
        __m_continental_steppe,
        __m_subtropical,
        __m_tropical,
        __m_continental_forest,
        __m_continental_steppe,
        __m_tropical,
    )

    k_tropical_world = (
        __semi_arid,
        __arid_desert,
        __k_tropical,
        __k_subtropical,
        __k_savanna,
        __k_mediterranean,
        __k_continental_steppe,
        __k_subtropical,
        __k_tropical,
        __k_continental_forest,
        __k_continental_steppe,
        __k_tropical,
    )

    g_tropical_world = (
        __semi_arid,
        __arid_desert,
        __g_tropical,
        __g_subtropical,
        __g_savanna,
        __g_mediterranean,
        __g_continental_steppe,
        __g_subtropical,
        __g_tropical,
        __g_continental_forest,
        __g_continental_steppe,
        __g_tropical,
    )

    a_tropical_world = (
        __semi_arid,
        __arid_desert,
        __a_tropical,
        __rocky,
        __a_savanna,
        __a_mediterranean,
        __rocks,
        __a_subtropical,
        __mountains,
        __rocky,
        __a_continental_steppe,
        __mountains,
    )

    f_tropical_world = (
        __semi_arid,
        __arid_desert,
        __f_tropical,
        __f_subtropical,
        __f_savanna,
        __f_mediterranean,
        __f_continental_steppe,
        __f_subtropical,
        __f_tropical,
        __f_continental_forest,
        __rocky,
        __f_tropical,
    )



    m_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __m_savanna,
        __m_savanna,
        __semi_arid,
        __m_subtropical,
        __m_tropical,
        __semi_arid,
        __m_mediterranean,
        __mountains,
    )

    k_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __k_savanna,
        __k_savanna,
        __semi_arid,
        __k_subtropical,
        __k_tropical,
        __semi_arid,
        __k_mediterranean,
        __mountains,
    )

    g_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __g_savanna,
        __g_savanna,
        __semi_arid,
        __g_subtropical,
        __g_tropical,
        __semi_arid,
        __g_mediterranean,
        __mountains,
    )

    a_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __a_savanna,
        __arid_desert,
        __semi_arid,
        __a_subtropical,
        __a_tropical,
        __semi_arid,
        __a_mediterranean,
        __mountains,
    )

    f_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __f_savanna,
        __rocky,
        __semi_arid,
        __f_subtropical,
        __f_tropical,
        __semi_arid,
        __f_mediterranean,
        __mountains,
    )

    @staticmethod
    def WaterLevelIncrease(s):
        return (s=="k")*0.2 + (s=="f")*(-0.2) + (s=="a")*(-0.4)
    
    @staticmethod
    def WaterDepthIncrease(g):
        depth = 0
        if g < 1 and g >= 0.5:
            return 0.1
        elif g >= 0 and g < 0.5:
            return 0.25
        elif g == 1:
            return 1
        elif g > 1 and g < 1.5:
            return -0.1
        elif g>=1.5 and g<2:
            return -0.25
        else:
            return -0.5
        
    @staticmethod
    def CloudVariation(t, flux, g):
        cloud_variation = 0

        if t < -30:
            cloud_variation += 0.2
        elif t < 0:
            cloud_variation += 0.1
        elif t < 10:
            cloud_variation += 0
        elif t < 22:
            cloud_variation -= 0.1
        elif t < 36:
            cloud_variation -= 0.2
        
        if g < 1 and g >= 0.5:
            cloud_variation -= 0.05
        elif g >= 0 and g < 0.5:
            cloud_variation -= 0.1
        elif g == 1:
            cloud_variation += 0
        elif g > 1 and g < 1.5:
            cloud_variation += 0.05
        elif g>=1.5 and g<2:
            cloud_variation += 0.1

        if flux>=1.5:
            cloud_variation -= 0.05
        elif flux<=0.5:
            cloud_variation += 0.05


        return cloud_variation