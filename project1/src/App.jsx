import './App.css'
import { useState, useEffect, useRef } from 'react';
import Viewer from '../component/Viewer';
import Controllar from '../component/Controller';
import Even from '../component/Even';
import Eten from '../component/Eten';

function App() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");
  const handleSetCount = (value) =>{
    setCount(count+value);
  };
  const handleChangeText = (e)=>{
    setText(e.target.value);
  };
  const didMountRef = useRef(false);

  useEffect(()=>{
    if (!didMountRef.current){
      didMountRef.current = true;
      return;
    }else{
     console.log("컴포넌트 업데이트!"); 
    }
  });

  useEffect(()=>{
    console.log("컴포넌트 마운트");
  },[]);
  useEffect(()=>{
      const intervalID = setInterval (()=>{
        console.log("깜빡");
      }, 1000);


      return ()=>{
        console.log("클린업");
        clearInterval(intervalID);
      };
  });

  return ( <div className='app'>
    <h1>Simple Counter</h1>
    <section>
      <input value={text} onChange={handleChangeText}/>
      <Viewer count ={count} />
      {count % 2 === 0 && <Even />}
      {count % 2 === 1 && <Eten />}

      <Controllar handleSetCount={handleSetCount} />
    </section>
  </div>
  );
}

export default App
