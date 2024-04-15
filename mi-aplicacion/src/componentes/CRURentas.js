import React, { useState } from 'react';
import { eliminarRenta } from '../crudFunctions';
import { rentasData } from '../data';
import './CRURentas.css';

const CRURentas = () => {
  const [idPelicula, setIdPelicula] = useState('');
  const [diasRenta, setDiasRenta] = useState('');
  const [rentaEditando, setRentaEditando] = useState(null);
  const [rentas, setRentas] = useState(rentasData);

  const handleAgregarEditarRenta = () => {
    const idPeliculaEntero = parseInt(idPelicula);
    
    if (rentaEditando !== null) {
      const rentasActualizadas = rentas.map(renta => {
        if (renta.id === rentaEditando) {
          return {
            ...renta,
            idPelicula: idPeliculaEntero,
            diasRenta: parseInt(diasRenta)
          };
        }
        return renta;
      });
      setRentas(rentasActualizadas);
      setIdPelicula('');
      setDiasRenta('');
      setRentaEditando(null);
    } else {
      setRentas([...rentas, { id: rentas.length + 1, idPelicula: idPeliculaEntero, diasRenta: parseInt(diasRenta) }]);
      setIdPelicula('');
      setDiasRenta('');
    }
  };

  const handleSeleccionarRenta = (renta) => {
    setIdPelicula(renta.idPelicula ? renta.idPelicula.toString() : '');
    setDiasRenta(renta.diasRenta ? renta.diasRenta.toString() : '');
    setRentaEditando(renta.id);
  };

  const handleEliminarRenta = (id) => {
    if (rentaEditando === id) {
      return;
    }
    const rentasFiltradas = rentas.filter(renta => renta.id !== id);
    setRentas(rentasFiltradas);
    eliminarRenta(id); // Asegúrate de eliminar la renta en tu lógica de backend
  };

  return (
    <div className="crud-rentas-container">
      <h2>CRU de Rentas</h2>
      <div className="crud-rentas-form">
        <h3>{rentaEditando ? 'Editar Renta' : 'Agregar Renta'}</h3>
        <input type="number" placeholder="ID Película" value={idPelicula} onChange={(e) => setIdPelicula(e.target.value)} />
        <input type="number" placeholder="Días de Renta" value={diasRenta} onChange={(e) => setDiasRenta(e.target.value)} />
        <button onClick={handleAgregarEditarRenta}>{rentaEditando ? 'Editar Renta' : 'Agregar Renta'}</button>
      </div>
      <div>
        <h3>Lista de Rentas</h3>
        <ul className="crud-rentas-list">
          {rentas.map(renta => (
            <li key={renta.id} className="crud-rentas-item">
              ID Película: {renta.idPelicula} - Días de Renta: {renta.diasRenta}
              <button onClick={() => handleSeleccionarRenta(renta)}>Editar</button>
              <button onClick={() => handleEliminarRenta(renta.id)} disabled={rentaEditando === renta.id}>Eliminar</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default CRURentas;