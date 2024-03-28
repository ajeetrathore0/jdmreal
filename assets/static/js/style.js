document.querySelector('.usericon img').addEventListener('click',(e)=>{
    document.querySelector('.loginsignup').classList.toggle('loginsignupshow')
})

window.onclick=function(e){
if(e.y>70){
    document.querySelector('.loginsignup').classList.remove('loginsignupshow')
}
}


document.querySelector('#login').addEventListener('click',(e)=>{
    document.querySelector('#loginsignuparea').classList.add('loginsignupareashow')
})

document.querySelector('#closeloginsignuparea').addEventListener('click',()=>{
    document.querySelector('#loginsignuparea').classList.remove('loginsignupareashow')
})

let navli=document.querySelectorAll('.menubar li');

navli.forEach(elem=>{
    elem.addEventListener('click',(e)=>{
        navli.forEach(elems=>{
            elems.classList.remove('activeli')
        })
        elem.classList.add('activeli');
    })
})