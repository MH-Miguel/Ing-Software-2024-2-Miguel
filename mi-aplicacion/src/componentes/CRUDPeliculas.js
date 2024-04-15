import React, { useState } from 'react';
import { peliculasData } from '../data';
import { agregarPelicula, eliminarPelicula } from '../crudFunctions';
import './CRUDPeliculas.css';

const CRUDPeliculas = () => {
  const [nombre, setNombre] = useState('');
  const [genero, setGenero] = useState('');
  const [duracion, setDuracion] = useState('');
  const [inventario, setInventario] = useState('');
  const [peliculaEditando, setPeliculaEditando] = useState(null);
  const [peliculas, setPeliculas] = useState(peliculasData); // Actualizar el estado con la lista de películas

  const handleAgregarEditarPelicula = () => {
    if (peliculaEditando !== null) {
      // Editar película existente
      const peliculasActualizadas = peliculas.map(pelicula => {
        if (pelicula.id === peliculaEditando) {
          return {
            ...pelicula,
            nombre,
            genero,
            duracion: parseInt(duracion),
            inventario: parseInt(inventario),
          };
        }
        return pelicula;
      });
      setPeliculas(peliculasActualizadas);
      // Reiniciar campos y estado de edición
      setNombre('');
      setGenero('');
      setDuracion('');
      setInventario('');
      setPeliculaEditando(null);
    } else {
      // Agregar nueva película
      const nuevaPelicula = {
        id: peliculas.length + 1,
        nombre,
        genero,
        duracion: parseInt(duracion),
        inventario: parseInt(inventario),
      };
      setPeliculas([...peliculas, nuevaPelicula]);
      // Reiniciar campos
      setNombre('');
      setGenero('');
      setDuracion('');
      setInventario('');
    }
  };

  const handleSeleccionarPelicula = (pelicula) => {
    // Establecer la película seleccionada para edición
    setNombre(pelicula.nombre);
    setGenero(pelicula.genero);
    setDuracion(pelicula.duracion.toString());
    setInventario(pelicula.inventario.toString());
    // Establecer el ID de la película para editar
    setPeliculaEditando(pelicula.id);
  };

  const handleEliminarPelicula = (id) => {
    // Eliminar la película de la lista simulada
    eliminarPelicula(id);
    // Actualizar el estado con la lista de películas excluyendo la película eliminada
    setPeliculas(peliculas.filter(pelicula => pelicula.id !== id));
    // Reiniciar campos si la película eliminada está en modo de edición
    if (peliculaEditando === id) {
      setNombre('');
      setGenero('');
      setDuracion('');
      setInventario('');
      setPeliculaEditando(null);
    }
  };

  return (
    <div className="crud-peliculas-container"> {/* Añade la clase CSS al contenedor principal */}
      <h2>CRUD de Películas</h2>
      <div className="crud-peliculas-form"> {/* Añade la clase CSS al formulario */}
        <h3>{peliculaEditando ? 'Editar Película' : 'Agregar Película'}</h3>
        <input type="text" placeholder="Nombre" value={nombre} onChange={(e) => setNombre(e.target.value)} />
        <input type="text" placeholder="Género" value={genero} onChange={(e) => setGenero(e.target.value)} />
        <input type="number" placeholder="Duración" value={duracion} onChange={(e) => setDuracion(e.target.value)} />
        <input type="number" placeholder="Inventario" value={inventario} onChange={(e) => setInventario(e.target.value)} />
        <button onClick={handleAgregarEditarPelicula}>{peliculaEditando ? 'Editar Película' : 'Agregar Película'}</button>
      </div>
      <div>
        <h3>Lista de Películas</h3>
        <ul className="crud-peliculas-list"> {/* Añade la clase CSS a la lista */}
          {peliculas.map(pelicula => (
            <li key={pelicula.id} className="crud-peliculas-item"> {/* Añade la clase CSS a cada elemento de la lista */}
              {pelicula.nombre} - {pelicula.genero} ({pelicula.duracion} mins) - Inventario: {pelicula.inventario}
              <button onClick={() => handleSeleccionarPelicula(pelicula)}>Editar</button>
              <button onClick={() => handleEliminarPelicula(pelicula.id)} disabled={peliculaEditando === pelicula.id}>Eliminar</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default CRUDPeliculas;