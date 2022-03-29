from pywebio import *


def main():  # PyWebIO application function
    output.put_markdown(r""" # MovieRec """)
    output.put_text("Protótipo de Sistema de Recomendação de filmes")


if __name__ == '__main__':
    start_server(main, port=80)