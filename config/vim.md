# Vim

---

### Overview
Vim이 짱
어느 컴퓨터에서도 바로 활용할 수 있도록 프로젝트 만들기 install.sh까지

### Build
- [Vundle](https://github.com/VundleVim/Vundle.vim) 설치
- [vimrc](https://github.com/oognus/vim.git) 설치 - vimrc만 있어도 되나?

### How to use

**Insert mode**
`Ctrl+n`: auto complete
`i` `I`
`a` `A`
`o` `O`

**Cut & Paste**
`d` `D`: delete to the end of the line

**Move**
`w`
`b`
`gg` `G`
`^`
`$`

**Tips**
- `"+`는 클립보드로 `y`는 복사 `p`는 붙여넣기

[v] dd 하는데 라인은 그대로 유지하려면? - `0D`  
[x] 문장 위치 이동
[x] 한글 지우는거 여전히 문제
[x] copy to clipboard - `"+y`
[ ] INSERT모드에서 이동이 필요할 때 화살표를 활용하나? 아니면 NORMAL모드로 전환 후 hjkl를 사용하나?
[v] Vim 안에서 git 활용법
[ ] devtaste
[ ] 프로젝트 전체 검색
[ ] Markdown preview
[ ] Search / Replace
[ ] 들여쓰기 하면서 입력
[ ] 느림
[ ] 기존 프로젝트 들여쓰기 문제




By default, the table contains RGB values of terminal colors as displayed by
iTerm2 on macOS. If you're using another terminal emulator (urxvt,
xfce4-terminal,... pretty much any terminal on Linux), the colors aren't
displayed in the same way. That's why you may see a difference in color of GUI
and terminal [n]vim in Linux.

If `let g:seoul256_srgb` is set to 1, the color mapping is altered
to suit the way urxvt (and various other terminals) renders them. That way, the
colors of the terminal and GUI versions are uniformly colored on Linux.
