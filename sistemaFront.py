from pywebio import *
from pywebio.output import *

def main():  # PyWebIO application function

    put_markdown(r""" # MovieRec """)
    put_text("Protótipo de Sistema de Recomendação de filmes")

    put_table([
    ['Type', 'Content'],
    ['html', put_html('X<sup>2</sup>')],
    ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
    ['buttons', put_buttons(['A', 'B'], onclick=...)],  
    ['markdown', put_markdown('`Awesome PyWebIO!`')],
    ['file', put_file('hello.text', b'hello world')],
    ['table', put_table([['A', 'B'], ['C', 'D']])]
    ])

if __name__ == '__main__':
    start_server(main, port=80)