import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import CRUDClientes from './componentes/CRUDClientes';
import CRUDPeliculas from './componentes/CRUDPeliculas';
import CRURentas from './componentes/CRURentas';
import './App.css';


const App = () => {
  return (
    <Router>
      <div className="container"> {/* Agrega la clase container para aplicar los estilos */}
        <h1>Sistema de Administración de Alquiler de Películas</h1>
        <nav>
          <ul>
            <li>
              <a href="/">Vista Principal</a>
            </li>
            <li>
              <a href="/clientes">CRUD Clientes</a>
            </li>
            <li>
              <a href="/peliculas">CRUD Películas</a>
            </li>
            <li>
              <a href="/rentas">CRU Rentas</a>
            </li>
          </ul>
        </nav>

        <hr />

        <Routes>
          <Route path="/clientes" element={<CRUDClientes />} />
          <Route path="/peliculas" element={<CRUDPeliculas />} />
          <Route path="/rentas" element={<CRURentas />} />
          {/* Mostrar texto o HTML directamente */}
          <Route path="/" element={<h2>Bienvenido a la Vista Principal</h2>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
