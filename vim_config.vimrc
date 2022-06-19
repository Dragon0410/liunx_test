set number									"显示行号
syntax on									"语法高亮
set autoindent									"自动对齐
set smartindent									"根据上面的格式，智能选择对齐方式
set tabstop=4									"tab健为4各空格
set shiftwidth=4								"
set showmatch									"匹配模式
set cursorline									"光标所在行高亮
highlight CursorLine cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE

"自动匹配
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {}<ESC>i
inoremap < <><ESC>i
inoremap " ""<ESC>i
inoremap ' ''<ESC>i
inoremap ` ''''''<ESC>


set statusline=%1*\%<%.50F\

autocmd BufNewFile *.py,*.tex exec ":call SetTitle()"
func! SetTitle() 
    if &filetype == 'python'
        call setline(1,"#!/usr/bin/env python3")
        call append(line("."),"# -*- coding:UTF-8 -*-")
        call append(line(".")+1, "# File Name: ".expand("%"))
        call append(line(".")+2, "# Author: stubborn vegeta")
        call append(line(".")+3, "# Created Time: ".strftime("%c"))
        call append(line(".")+4, "##########################################################################")
        call append(line(".")+5, "")
        call append(line(".")+6, "def main(): pass")
        call append(line(".")+7, "")
        call append(line(".")+8, "if __name__ == '__main__':")
        call append(line(".")+9, "    main()")
    endif
    normal Go 
endfunc
