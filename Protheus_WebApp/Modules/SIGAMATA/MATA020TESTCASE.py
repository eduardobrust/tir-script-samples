from tir import Webapp
import unittest

class MATA020(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAMATA','11/04/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA020')

	def test_MATA020_CT001_Inclusao(self):
		"""Teste de Inclusão - Create de um novo fornecedor"""
		codigo = 'F00001'
		loja = '01'
		razao_social = 'FORNECEDOR SÃO PAULO LTDA'
		tipo = 'F'

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.ClickFolder('Cadastrais')
		self.oHelper.SetValue('A2_COD', codigo)
		self.oHelper.SetValue('A2_LOJA', loja)
		self.oHelper.SetValue('A2_NOME', razao_social)
		self.oHelper.SetValue('A2_TIPO', tipo)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')

		self.oHelper.AssertTrue()

	def test_MATA020_CT002_Visualizacao(self):
		"""Teste de Visualização - Read de um fornecedor existente"""
		codigo = 'F00001'
		loja = '01'
		razao_social = 'FORNECEDOR SÃO PAULO LTDA'
		tipo = 'F'

		self.oHelper.SearchBrowse(f'D MG    {codigo+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A2_COD', codigo)
		self.oHelper.CheckResult('A2_LOJA', loja)
		self.oHelper.CheckResult('A2_NOME', razao_social)
		self.oHelper.CheckResult('A2_TIPO', tipo)

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA020_CT003_Alteracao(self):
		"""Teste de Alteração - Update de um fornecedor"""
		codigo = 'F00001'
		loja = '01'
		razao_social_alterada = 'FORNECEDOR SÃO PAULO ALTERADO LTDA'

		self.oHelper.SearchBrowse(f'D MG    {codigo+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Alterar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.SetValue('A2_NOME', razao_social_alterada)

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')

		self.oHelper.SearchBrowse(f'D MG    {codigo+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Cadastrais')

		self.oHelper.CheckResult('A2_NOME', razao_social_alterada)

		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA020_CT004_Exclusao(self):
		"""Teste de Exclusão - Delete de um fornecedor"""
		codigo = 'F00001'
		loja = '01'

		self.oHelper.SearchBrowse(f'D MG    {codigo+loja}', 'Filial+codigo + Loja')
		self.oHelper.SetButton('Outras Ações')
		self.oHelper.SetButton('Excluir')

		self.oHelper.SetButton('Sim')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
