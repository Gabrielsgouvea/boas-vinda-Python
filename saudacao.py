# -*- coding: utf-8 -*-

###########################################################################
## Código com Nome, Idade e Cálculo de Nascimento
###########################################################################

import wx
import wx.xrc
import datetime # Importamos para saber o ano atual automaticamente

import gettext
_ = gettext.gettext

###########################################################################

class saldacao ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Py_Robot 2.0", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bs_organize = wx.BoxSizer( wx.VERTICAL )

        # Pergunta do Nome
        self.stt_pergunta = wx.StaticText( self, wx.ID_ANY, _(u"Olá! Eu sou o Py_Robot. Qual o seu nome?"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bs_organize.Add( self.stt_pergunta, 0, wx.ALL, 5 )

        self.ent_responde = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bs_organize.Add( self.ent_responde, 0, wx.ALL, 5 )

        # Pergunta da Idade
        self.stt_idade = wx.StaticText( self, wx.ID_ANY, _(u"Qual a sua idade?"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bs_organize.Add( self.stt_idade, 0, wx.ALL, 5 )

        self.ent_idade = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bs_organize.Add( self.ent_idade, 0, wx.ALL, 5 )

        # Botão
        self.bt_ok = wx.Button( self, wx.ID_ANY, _(u"Responder"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bs_organize.Add( self.bt_ok, 0, wx.ALL, 5 )

        self.SetSizer( bs_organize )
        self.Layout()
        self.Centre( wx.BOTH )

        # Connect Events
        self.bt_ok.Bind( wx.EVT_BUTTON, self.clicou_botao )

    def __del__( self ):
        pass

    # A LÓGICA DO ROBÔ
    def clicou_botao( self, event ):
        # 1. Pega os dados das caixas
        nome = self.ent_responde.GetValue()
        texto_idade = self.ent_idade.GetValue()
        
        # 2. Verifica se a idade é um número para não dar erro
        if texto_idade.isdigit():
            idade = int(texto_idade)
            ano_atual = datetime.date.today().year
            nascimento = ano_atual - idade
            
            # 3. Cria a mensagem personalizada
            mensagem = (f"Olá {nome}!\n\n"
                        f"Pelas minhas contas de robô, você nasceu em {nascimento}.\n"
                        f"Seja bem-vindo ao Python!")
            
            tipo_icone = wx.ICON_INFORMATION
        else:
            mensagem = "Por favor, digite apenas números na idade!"
            tipo_icone = wx.ICON_ERROR

        # 4. Exibe o resultado
        wx.MessageBox(mensagem, "Resposta do Robô", wx.OK | tipo_icone)
        event.Skip()

if __name__ == "__main__":
    app = wx.App()
    frame = saldacao(None)
    frame.Show()
    app.MainLoop()
