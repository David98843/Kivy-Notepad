from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog

Window.size = (300, 600)

KV = '''
<ListItem>:
    cols : 2
    size_hint : (1,None)
    pos_hint : {'center_x' : .5, 'center_y' : .5}

    MDCard:
        elevation : 2
        md_bg_color : 'whitesmoke'

        MDCheckbox:
            size_hint : (0.2,1)
            _no_ripple_effect : True
            color : 'cornflowerblue'
            color_active : 'cornflowerblue'
            color_inactive : 'cornflowerblue'

        MDTextField:
            border : 'red'
            mode : 'fill'
            padding : (10,30)
            text_color_normal : "black"
            hint_text_color_normal : 'cornflowerblue'
            hint_text_color_focus : 'cornflowerblue'
            text_color_focus : 'black'
            fill_color_normal : 'whitesmoke'
            fill_color_focus : 'whitesmoke'
            mode : 'fill'
            active_line : ''
            hint_text : 'Enter some text'
            pos_hint : {'center_x': .2, 'center_y' : .5}

Screen:

    MDGridLayout:
        cols : 1
            
        MDTopAppBar:
            title : 'TodoList'
            size_hint : (1.0, None)
            elevation : 0
            right_action_items : [['plus', lambda x: app.add_todo()],['cog',lambda x : app.changeTheme()]]

        ScrollView:
            do_scroll_y : True
            do_scroll_x : False
            size_hint_y : .85
            pos_hint : {'center_x' : .5, 'y' : 0}
            bar_width : 0

            MDGridLayout:
                cols : 1
                size_hint_y : None
                height : self.minimum_height
                row_default_height : 2
                padding : (15, 10)
                spacing : (15, 20)
                id : todo_list

'''

class ListItem(MDGridLayout):
   pass 


class demoApp(MDApp):

    def build(self):
        self.icon = 'huggingface_logo-noborder.png'

        self.screen = Builder.load_string(KV)  
        
        self.on_start = self.showMessage

        return self.screen

    def add_todo(self):
        
        self.screen.ids.todo_list.add_widget(ListItem())

    def showMessage(self):

        close_btn = MDFlatButton(
            text = 'Ok',
        )
        leave_btn = MDFlatButton(
            text = 'Leave'
        )

        intro_dialog = MDDialog(
            text = 'Hello User, this is a todo-list app, press the plus button to add new items',
            buttons = [leave_btn, close_btn]
        )
        intro_dialog.open()

        close_btn.on_release = intro_dialog.dismiss
        leave_btn.on_release = self.stop

    def changeTheme(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'




demoApp().run()