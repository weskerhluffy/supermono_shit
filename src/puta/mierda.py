'''
Created on 10/07/2017

@author: 
'''

import logging
import sys
from collections import Counter
nivel_log = logging.ERROR
# nivel_log = logging.DEBUG
logger_cagada = None

def imprime_edificios_parados(edificios):
    cadena = ""
    for idx_piso in range(len(edificios[0]) - 1, 0, -1):
        cadena += "\t".join([str(edif[idx_piso]) for edif in edificios]) + "\n"
    return cadena


def supermono_mierda_core(edificios, brinco_deficit):
    max_edificios = 0
    salvados_dp = [[0] * len(edificios[0]) for _ in range(len(edificios))]
    primer_piso_dp = len(edificios[0]) - 1
    max_por_piso = [0] * (len(edificios[0]) + 1)
    
    for idx, _ in enumerate(edificios):
        salvados_dp[idx][primer_piso_dp ] = edificios[idx][primer_piso_dp ]
        
    piso_invalidos = 1
    while(piso_invalidos < brinco_deficit):
        for idx, _ in enumerate(edificios):
            salvados_dp[idx][primer_piso_dp - piso_invalidos] += salvados_dp[idx][primer_piso_dp - piso_invalidos + 1] + edificios[idx][primer_piso_dp - piso_invalidos]
        piso_invalidos += 1
        
    primer_piso_dp -= piso_invalidos
    
    logger_cagada.debug("l 1er piso caca %s" % primer_piso_dp)
    
#    for idx_piso in range(len(edificios[0]) - 1, 0, -1):
    for idx_piso in range(len(edificios[0]) - 1, primer_piso_dp, -1):
        max_por_piso[idx_piso] = max([edificio[idx_piso] for edificio in edificios])

    logger_cagada.debug("los maximos x piso %s" % max_por_piso)
    
    for idx_piso in range(primer_piso_dp, 0, -1):
        for idx_edificio, edificio in enumerate(edificios):
            logger_cagada.debug("llenando edif %s piso %s" % (idx_edificio, idx_piso))
            salvados_dp[idx_edificio][idx_piso] = max(salvados_dp[idx_edificio][idx_piso + 1], max_por_piso[idx_piso + brinco_deficit])
            salvados_dp[idx_edificio][idx_piso] += edificio[idx_piso]
        max_por_piso[idx_piso] = max([salvados[idx_piso] for salvados in salvados_dp])
            
    logger_cagada.debug("los salvados dp\n%s" % imprime_edificios_parados(salvados_dp))
    max_edificios = max([salvados[1] for salvados in salvados_dp])
    
    return max_edificios

def supermono_mierda_main():
    lineas = list(sys.stdin)
    edificios = []
    
    num_edificios, altura, brinco_deficit = [int(caca) for caca in lineas[0].strip().split(" ")]
    
    edificios = [[0] * (altura + 1) for _ in range(num_edificios)]
    
    for idx_edificio, linea in enumerate(lineas[1:]):
        personas = Counter(filter(lambda x:x, map(lambda mierda:int(mierda), linea.strip().split(" ")[1:])))
        for idx_piso in personas:
            edificios[idx_edificio][idx_piso] = personas[idx_piso]
            
    logger_cagada.debug("los edificios kedaron\n%s" % imprime_edificios_parados(edificios))
    caca = supermono_mierda_core(edificios, brinco_deficit)
    
    logger_cagada.debug("el maximo caca %s" % caca)
    print(caca)

if __name__ == '__main__':
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
        logging.basicConfig(level=nivel_log, format=FORMAT)
        logger_cagada = logging.getLogger("asa")
        logger_cagada.setLevel(nivel_log)

        supermono_mierda_main()
