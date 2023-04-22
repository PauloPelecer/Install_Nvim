set number
set mouse=a
" Configurações básicas
set number                       " Exibe números de linha               " Exibe números de linha relativos
set tabstop=4                    " Define o tamanho do tab como 4 espaços
set shiftwidth=4                 " Define o tamanho da indentação como 4 espaços
set expandtab                    " Converte tab em espaços
set cursorline                   " Exibe uma linha vertical sob o cursor

" Configurações de cores e tema
syntax on                        " Ativa a syntax highlighting
set termguicolors                " Ativa cores verdadeiras no terminal
let g:gruvbox_material_background = 'hard'    " Define o fundo como "hard"

" Plugins e gerenciadores de plugins
call plug#begin('~/.vim/plugged')  " Define o diretório de plugins
Plug 'tpope/vim-commentary'        " Ativa comentários mais facilmente
Plug 'windwp/nvim-autopairs'
Plug 'preservim/nerdtree'          " Ativa o gerenciador de arquivos

Plug 'dracula/vim', { 'as': 'dracula' }
Plug 'vim-airline/vim-airline'     " Ativa a barra de status
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()                    " Termina a definição de plugins
color dracula
" Mapeamentos de teclado personalizados
" Use o prefixo <leader> para todos os mapeamentos personalizados
let mapleader = ","               " Define o prefixo como ","

" Ativa o NERDTree com o mapeamento <leader>n
nnoremap <leader>n :NERDTreeToggle<CR>

" Ativa comentários com o mapeamento <leader>c
nmap <leader>c <Plug>CommentaryLine
set guifont=NomeDaSuaFonte:h11

" Ativa a barra de status do Vim Airline
let g:airline_powerline_fonts = 1
let g:airline_theme = 'dracula'
let g:airline#extensions#tabline#enabled = 1
let g:coc_disable_startup_warning = 1
" Habilitar nvim-autopairs
lua << EOF
  require'nvim-autopairs'.setup()
EOF




