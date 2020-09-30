function chooseRandomWord(list) {
    let random = Math.random() * list.length
    random = Math.floor(random)
    return list[random]
}

let textField = document.getElementById("autotype")

function typeWord(word, index, typing) {
    if (typing) {
        textField.innerText = word.substr(0, index)
    } else {
        textField.innerText = word.substr(0, word.length - index)
    }
}

function start() {
    let typing = true
    let index = 1

    let words = ["sudo apt-get", "history | grep 'gcc'", "vim script.js", "find ~ -iname '*.py' -o -iname '*.cpp'", "Dragos Ionescu", "\"Hello, World!\""]
    let word = chooseRandomWord(words)
    let myInterval = setInterval(() => {
        typeWord(word, index, typing)

        index++
        if (index >= word.length + 5) {
            if (typing) {
                typing = false
            } else {
                word = chooseRandomWord(words)
                typing = true
            }
            index = 0
        }
     }, 100)
}

start()
