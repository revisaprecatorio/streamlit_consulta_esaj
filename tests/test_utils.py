"""
Testes para o módulo utils
"""
import unittest
import sys
import os

# Adicionar o diretório src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import normalizar_cpf, validar_cpf

class TestUtils(unittest.TestCase):
    """Testes para funções utilitárias"""
    
    def test_normalizar_cpf(self):
        """Testa a normalização de CPF"""
        # CPF com 9 dígitos
        self.assertEqual(normalizar_cpf("123456789"), "00123456789")
        
        # CPF com 10 dígitos
        self.assertEqual(normalizar_cpf("1234567890"), "01234567890")
        
        # CPF com 11 dígitos
        self.assertEqual(normalizar_cpf("12345678901"), "12345678901")
        
        # CPF com caracteres especiais
        self.assertEqual(normalizar_cpf("123.456.789-01"), "12345678901")
        
        # CPF com mais de 11 dígitos
        self.assertEqual(normalizar_cpf("123456789012"), "12345678901")
    
    def test_validar_cpf(self):
        """Testa a validação de CPF"""
        # CPF válido
        self.assertTrue(validar_cpf("11144477735"))
        
        # CPF inválido (todos os dígitos iguais)
        self.assertFalse(validar_cpf("11111111111"))
        
        # CPF inválido (dígitos verificadores incorretos)
        self.assertFalse(validar_cpf("12345678901"))
        
        # CPF com menos de 11 dígitos (deve ser normalizado primeiro)
        self.assertFalse(validar_cpf("123456789"))

if __name__ == '__main__':
    unittest.main()
