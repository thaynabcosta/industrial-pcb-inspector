import cv2
import numpy as np
from configuracao import (
    IMAGEM_PRINCIPAL,
    TEMPLATE,
    LIMITE_DE_CONFIANCA,
    COR_DETECCAO
)

def realizar_inspecao():
    """
    Carrega as imagens e executa o Template Matching para 
    detectar um componente na posição correta.
    """
    try:
        imagem_principal = cv2.imread(IMAGEM_PRINCIPAL, cv2.IMREAD_COLOR)
        template = cv2.imread(TEMPLATE, cv2.IMREAD_COLOR)

        if imagem_principal is None:
            print(f"ERRO: Não foi possível carregar a imagem principal: {IMAGEM_PRINCIPAL}")
            return
        if template is None:
            print(f"ERRO: Não foi possível carregar o template: {TEMPLATE}")
            return

        altura_template, largura_template, _ = template.shape
        resultado = cv2.matchTemplate(imagem_principal, template, cv2.TM_CCOEFF_NORMED)

        _, max_confianca, _, max_loc = cv2.minMaxLoc(resultado)
        print(f"-> Confiança Máxima Encontrada: {max_confianca:.2f}")


        if max_confianca >= LIMITE_DE_CONFIANCA:
            print("\n✅ PRODUTO APROVADO: Componente Encontrado na Posição Correta!")
        
            canto_superior_esquerdo = max_loc
            
            canto_inferior_direito = (
                canto_superior_esquerdo[0] + largura_template, 
                canto_superior_esquerdo[1] + altura_template
            )

            cv2.rectangle(
                imagem_principal, 
                canto_superior_esquerdo, 
                canto_inferior_direito, 
                COR_DETECCAO, 
                2
            )

        else:
            print("\n❌ PRODUTO REPROVADO: Componente Ausente ou Fora de Posição/Defeituoso!")
            
        cv2.imshow('Resultado da Inspecao', imagem_principal)
        cv2.waitKey(0)
        
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Ocorreu um erro durante a inspeção: {e}")


if __name__ == "__main__":
    realizar_inspecao()
    