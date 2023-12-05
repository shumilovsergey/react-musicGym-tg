import pizzaImg from "../images/pizza.png"
import burgerImg from "../images/burger.png"
import cocaImg from "../images/coca.png"
import saladImg from "../images/salad.png"
import waterImg from "../images/water.png"
import iceCreamImg from "../images/icecream.png"
import kebabImg from "../images/kebab.png"


export function getData() {
    return [
      { title: "Пицца", price: 650, Image: pizzaImg,id:1 },
      { title: "Бургер", price: 320, Image: burgerImg, id:2 },
      { title: "Кока-кола", price: 100, Image: cocaImg, id:3},
      { title: "Шашлык", price: 450, Image: kebabImg, id:4 },
      { title: "Салат", price: 180, Image: saladImg, id:5 },
      { title: "Вода", price: 49, Image: waterImg, id:6 },
      { title: "Айскрем", price: 60, Image: iceCreamImg, id:7 },
    ];
  }