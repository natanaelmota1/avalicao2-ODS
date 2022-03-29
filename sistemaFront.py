from pywebio import *
from pywebio.output import *

def main():  # PyWebIO application function
<<<<<<< HEAD
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
=======
    output.put_markdown(r""" # 🎥MovieRec """)
    output.put_text("Protótipo de Sistema de Recomendação de filmes")
>>>>>>> 3812a60c8dfe7255c82f6d408b8860686648d2ac


if __name__ == '__main__':
    start_server(main, port=80)