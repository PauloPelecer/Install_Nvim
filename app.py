import os
import subprocess as sub

class Config:
    def __init__(self):
        self.sys = os
        self.vim_plug = """sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'"""
        self.raiz = '/data/data/com.termux/files/home/'
        self.nodejs = '''curl -sL install-node.vercel.app/lts | bash '''
        self.coc_nvim = 'cd && cd .config/nvim/bundle && git clone https://github.com/neoclide/coc.nvim'

    def CreateDirs(self):
        self.sys.mkdir(f'{self.raiz}.config')
        self.sys.mkdir(f'{self.raiz}.config/nvim')
        self.sys.mkdir(f'{self.raiz}.config/nvim/plugged')


        self.sys.mkdir(f'{self.raiz}.config/nvim/bundle')
        return '\033[0;32mDiretorios de Configuraçoes Criados!\033[0m'


    def InstallCoc(self):
        self.sys.system(self.nodejs)
        self.sys.system(self.coc_nvim)
        self.sys.system('apt install yarn -y')
        return '\033[0;32mCoc.nvim Instalado Aguarde Vamos Instalar Mais Umas Dependencias!\033[0m'


    def InstallPlugVim(self):
        self.sys.system(self.vim_plug)
        return '\033[0;32mVim Plug Instalado Aguarde Vamos Instalar Mais Umas Dependencias!\033[0m'

    def InstallNeoVim(self):
        self.sys.system('apt install neovim -y')
        return '\033[0;32mNeoVim Aguarde Vamos Instalar Mais Umas Dependencias!\033[0m'

    def Install_initvim(self):
        with open('.init/init.vim', 'r') as file:
            data = file.read()
        with open(f'{self.raiz}.config/nvim/init.vim', 'w') as file:
            file.write(data)
        return '\033[0;32mTudo Configurado Para o Uso!\033[0m'



class dependencias:
    def __init__(self):
        pass
    def Command(self,cmd):
        try:
            os.system(cmd)
            return 'Download Concluido!'
        except:
            return f'Falha ao Executar :{cmd}\nContinuando a Instalação!'

    def RemoveConf(self):
        dependencias().Command('apt remove neovim')
        dependencias().Command('cd  && rm -rf .config')

        


if __name__ == '__main__':
    dependencias().RemoveConf()
    os.system('apt update && apt upgrade -y')
    os.system('apt remove yarn -y && apt remove nodejs -y')
    msg = Config().InstallPlugVim()
    print (msg)
    msg2 = Config().CreateDirs()
    print (msg2)
    msg3 = Config().InstallNeoVim()
    print (msg3)
    msg4 = Config().InstallCoc()
    print (msg4)
    msg5 = Config().Install_initvim()
    print (msg5)
