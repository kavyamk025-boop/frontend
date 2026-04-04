
// // let a=Boolean("/mvfk");
// // let b=false;
// // console.log(a);
// // console.log(b);
// // let c= Boolean(Number(Boolean("")));
// // console.log(c);
// // let d=String(Boolean(1));
// // console.log(d);

// // let g=undefined;
// // console.log(Boolean(typeof(g)))







// //  let a="kjdskd";
// //  let b="fhjhsfhdj";
// //  console.log(b.indexOf("j"));
// // console.log(b.at)
// // console.log()
// // console.log(a.search("k"))





// let revstr=[]
// let arr=["apple","mango","ravi","banana","grapes","shastry","pineapple"]
let arr=["ravi","shastry","mrunal","thakur","a","b","c","d",1,2,3,4,"$","#","%","@"]
let alpha=[]
let number=[]
let special=[]
let word=[]

for (let i=0;i<arr.length;i++){
 if(arr[i].length>1){
    word.push(arr[i])
 }
 if(arr[i].length==1){
    if("!@#$%^&*():".includes(arr[i])){
        special.push(arr[i])
    }
    else{
        alpha.push(arr[i])
    }
    
    }
   
  if(!isNaN(arr[i])){
        number.push(arr[i])}

}  
console.log(alpha);
console.log(number);
console.log(special);
console.log(word);
// let word=[]
// let Num=[]
// let alpha=[]
// let special=[]
// for(let i=0;i<arr.length;i++){
//     if(!isNaN(arr[i])){
//         Num.push(arr[i])
//     }
//     else if(arr[i].length==1){
//         if("!@$%^&*()?><|~".includes(arr[i])){
//          alpha.push(arr[i])
//         }
//         else{
// special.push(arr[i])
//         }
//     }

//     else{
//         word.push(arr[i])
//     }
// }
// console.log(word)
// console.log(alpha)
// console.log(Num)
// console.log(special)

















// let arrrev=[]
// for(let i=0;i<arr.length;i++){
//     let fun=revers(arr[i])
//     arrrev.push(fun)
// }
// console.log(arrrev)
// console.log(arr.reverse())

// let arrre=[]
// for(let i=arr.length-1;i>=0;i--){
//     let fun=revers(arr[i])
//     arrre.push(fun)
// }
// console.log(arrre.reverse())


// function revers(s){
//     let rev=""
//     for(let i=s.length-1;i>=0;i--){
//         rev+=s[i]
//     }
//     return rev
// }
















// for(let i=0;i<arr.length;i++){
    
//     if(arr[i]=="ravi" ){
//         revstr.push(rev(arr[i]))
//         }

//     else if(arr[i]=="shastry"){
//         revstr.push(rev(arr[i]))

//     }    
//         else{
//             revstr.unshift(arr[i])
//         }
//     }
    


// console.log(arr)


// function rev(s){
//     let rev=""
//     for(i=s.length-1;i>=0;i--){
        
//         if(i%2==0){
//             rev+=s[i].toUpperCase()}
//             else{
//                 rev+=s[i]
//             }
//     }
//     return rev
    
    
// }
// console.log(rev("kavya"))
