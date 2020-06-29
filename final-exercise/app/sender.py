from bottle import route, run , request

@route('/', method='POST')
def send():
    assunto = request.forms.get('subject')
    mensagem = request.forms.get('mensage')

    return 'Mensagem enfileirada ! Assunto: {} Mensagem: {}'.format(
        assunto, mensagem
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port=3000, debug=True)
