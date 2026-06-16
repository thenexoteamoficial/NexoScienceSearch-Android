from kivy.app import App
 fr om kivy.uix.boxlayout import BoxLayout
 fr om kivy.uix.textinput import TextInput
 fr om kivy.uix.label import Label
 fr om kivy.uix.button import Button
 fr om kivy.uix.scrollview import ScrollView
 fr om kivy.uix.gridlayout import GridLayout
 fr om kivy.clock import Clock

articles = [
    {"title": "Machine Learning in Climate Science", "author": "Dr. Elena Vargas", "year": "2025", "topic": "IA"},
    {"title": "Quantum Computing Applications", "author": "Prof. Marco Ruiz", "year": "2024", "topic": "Física"},
    {"title": "Advances in Renewable Energy Storage", "author": "Dr. Sofia Patel", "year": "2025", "topic": "Energía"},
    {"title": "Neural Networks for Medical Diagnosis", "author": "Dr. Carlos Mendoza", "year": "2024", "topic": "Medicina"},
    {"title": "Sustainable Agriculture and AI", "author": "Dra. Laura Kim", "year": "2025", "topic": "Agricultura"},
]

class SearchApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        
        # Título
        title = Label(text="NexoScienceSearch", font_size=32, bold=True, color=(0.2, 0.6, 1, 1))
        self.add_widget(title)
        
        # Barra de búsqueda
        self.search_input = TextInput(hint_text="Buscar artículos...", size_hint_y=None, height=50, font_size=20)
        self.search_input.bind(text=self.filter_articles)
        self.add_widget(self.search_input)
        
        # Contenedor de resultados
        self.results_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.results_layout.bind(minimum_height=self.results_layout.setter('height'))
        
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.results_layout)
        self.add_widget(scroll)
        
        self.show_articles(articles)
    
    def filter_articles(self, instance, text):
        filtered = [a for a in articles if text.lower() in a['title'].lower() or text.lower() in a['author'].lower()]
        self.show_articles(filtered)
    
    def show_articles(self, article_list):
        self.results_layout.clear_widgets()
        for art in article_list:
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=110, padding=10)
            box.add_widget(Label(text=art['title'], font_size=18, bold=True, color=(1,1,1,1)))
            box.add_widget(Label(text=f"{art['author']} • {art['year']} • {art['topic']}", font_size=14))
            self.results_layout.add_widget(box)

class NexoScienceSearchApp(App):
    def build(self):
        return SearchApp()

if __name__ == "__main__":
    NexoScienceSearchApp().run()