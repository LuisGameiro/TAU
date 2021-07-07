

function sum(a, b) {
    return a + b
}

console.log(sum(3, 5));

//anonymious function
setTimeout(function () { console.log("some text") }, 1000);

//arrow function
setTimeout(() => console.log("some text"), 1000);

/*
//object  deprecated
const objectVar = {
    id: 1303,
    object: "car",
    km: 17,
    "+weirdchar": 14,
    horn: function () { console.log(this.object + " makes beep beep"); }
};

objectVar.km = 19;

console.log(objectVar.id, objectVar.km);
console.log(objectVar["+weirdchar"]);
objectVar.horn();
*/
//Class 
class ClassTest {
    constructor(id, object) {
        this.id = id;
        this.object = object;
    };

    sound() {
        console.log(this.object + "makes puh puh");
    };
}

const car = new ClassTest(15, "truck");

car.sound();

// conditionals


function getName() {
    let name = document.getElementById("frm1");

    console.log("hello!!!" + name[0].value, name[1].value);

    salut(name[0].value, name[1].value);
}


function salut(fname, lname) {
    if (fname === "Luis" && lname === "Gameiro") {
        alert("hello My king!!!")
        window.location.href = "loops.html";
    }
    else {
        alert("go away peasent!!")
    }
}

function getNumber() {
    console.log(document.getElementById("prison")[0].value);
    let number = document.getElementById("prison")[0].value;

    for (let i = 0; i < number; i++) {
        setTimeout(() => { console.log("chasing prisioner: " + (i + 1)); document.getElementById("prison counting").innerHTML = i + 1; }, 2000);


    }
    document.getElementById("prison status").innerHTML = number + " in prision :)";

}
