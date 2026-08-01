import threading
import requests
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner

# URL DA API DO GEMINI
URL_IA = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key=AIzaSyDBa58Vo9Ixd6cel6p6nxFCXTtbjFOAHQM"

class TutorScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.card_digitando = None
        Clock.schedule_once(lambda dt: self.adicionar_balao("Tutor IA", "Olá! Sou o teu Tutor Cognitivo. Que desafio matemático ou computacional vamos investigar hoje?", "left"), 1)

    def enviar(self):
        msg = self.ids.input_msg.text
        if not msg.strip(): return
        self.ids.input_msg.text = ""
        self.adicionar_balao("Você", msg, "right")
        self.mostrar_digitando()
        threading.Thread(target=self.chamar_api, args=(msg,)).start()

    def mostrar_digitando(self):
        self.card_digitando = MDCard(size_hint=(0.4, None), height="50dp", padding="10dp", radius=[15, 15, 15, 0], md_bg_color=(0.9, 0.9, 0.9, 1))
        self.card_digitando.add_widget(MDSpinner(size_hint=(None, None), size=("20dp", "20dp"), active=True))
        self.ids.chat_list.add_widget(self.card_digitando)

    def chamar_api(self, msg):
        # ==========================================================
        # O CÉREBRO PEDAGÓGICO DO ALGOFIN (PROMPT DE SISTEMA)
        # ==========================================================
        contexto_pedagogico = (
            "Atue ESTRITAMENTE como um Tutor Cognitivo Socrático do aplicativo AlgoFin. "
            "Seu público são alunos do 9º ano. O seu objetivo é ensinar Matemática Financeira (Juros, Poupança, SAC) "
            "integrada ao Pensamento Computacional (Loops, Variáveis, Algoritmos). "
            "REGRAS ABSOLUTAS: "
            "1. NUNCA dê a resposta numérica final pronta. Seu papel é ser um 'andaime cognitivo'. "
            "2. MÉTODOS SOCRÁTICO: Sempre devolva uma pergunta reflexiva que faça o aluno pensar no próximo passo da resolução. "
            "3. DECOMPOSIÇÃO: Ajude o aluno a quebrar problemas grandes em partes menores (ex: identificar Capital, Taxa e Tempo). "
            "4. LINGUAGEM COMPUTACIONAL: Faça analogias entre o dinheiro e a programação (ex: 'O que acontece com a variável Saldo se o Loop do tempo aumentar?'). "
            "5. Responda de forma amigável, encorajadora e em no máximo 2 parágrafos curtos. "
            "Pergunta do aluno: "
        )
        
        payload = {
            "contents": [{
                "parts": [{"text": f"{contexto_pedagogico} {msg}"}]
            }]
        }
        
        try:
            r = requests.post(URL_IA, json=payload, timeout=12)
            txt = r.json()['candidates'][0]['content']['parts'][0]['text']
            
            # Limpeza e formatação de texto para o KivyMD
            txt = txt.replace('\\n', '\n').replace('\\\\n', '\n')
            txt = txt.replace('**', '[b]').replace('**', '[/b]')
            
            Clock.schedule_once(lambda dt: self.finalizar(txt))
        except:
            Clock.schedule_once(lambda dt: self.finalizar("Tive um pequeno problema de conexão. Podemos tentar analisar essa lógica novamente?"))

    def finalizar(self, texto):
        if self.card_digitando:
            self.ids.chat_list.remove_widget(self.card_digitando)
        self.adicionar_balao("Tutor IA", texto, "left")

    def adicionar_balao(self, autor, texto, lado):
        cor = (0.9, 0.9, 1, 1) if lado == "right" else (1, 1, 1, 1)
        card = MDCard(orientation="vertical", size_hint=(0.85, None), padding="12dp", radius=[15], md_bg_color=cor, pos_hint={lado: 1}, elevation=1)
        card.add_widget(MDLabel(text=f"[b]{autor}[/b]\n{texto}", markup=True, adaptive_height=True))
        card.bind(minimum_height=card.setter('height'))
        self.ids.chat_list.add_widget(card)
        Clock.schedule_once(lambda dt: setattr(self.ids.chat_scroll, 'scroll_y', 0))