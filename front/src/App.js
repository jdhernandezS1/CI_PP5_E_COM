import './App.css';
import Router from './Pages/Dashboard/Router';
import body from './Assets/Styles/Body.module.scss'

function App() {
  return (
    <div className={`${body.Standard} ` + "App"}>
      <Router />
    </div>
  );
}

export default App;
