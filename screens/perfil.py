from kivymd.uix.screen import MDScreen
from kivy.properties import BooleanProperty
from kivymd.app import MDApp

class PerfilScreen(MDScreen):
    edit_mode = BooleanProperty(False)

    def toggle_edit(self):
        self.edit_mode = not self.edit_mode
        app = MDApp.get_running_app()
        
        if not self.edit_mode:
            # Salvar dados ao fechar o modo de edição
            app.user_name = self.ids.field_nome.text
            app.escola = self.ids.field_escola.text
            app.turma = self.ids.field_turma.text
            app.save_data()
        
        self.ids.toolbar.right_action_items = [
            ["check" if self.edit_mode else "pencil", lambda x: self.toggle_edit()]
        ]

    def voltar(self):
        self.edit_mode = False
        self.manager.current = 'inicial'