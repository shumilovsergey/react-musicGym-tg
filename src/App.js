import './App.css';
import Button from './Components/Button/Button';
import Card from './Components/Card/Card';
const {getData} = require("./Components/db/db")

const foods = getData();

function App() {
  return (
    <>
    <h1 className='heading'>Магазинчик у Шумилова</h1>
    <div className='cards_container'>
      {foods.map((food) => {
        return <Card food={food} key={food.id}/>
      })}
    </div>
    </>
  );
}

export default App;
