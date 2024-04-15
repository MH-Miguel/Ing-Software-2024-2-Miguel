// Importar datos simulados
import { clientesData, peliculasData, rentasData } from './data';

// Función para agregar un cliente
export const agregarCliente = (nombre, apellidoPaterno, apellidoMaterno, email) => {
    const id = clientesData.length + 1;
    const nuevoCliente = { id, nombre, apellidoPaterno, apellidoMaterno, email };
    clientesData.push(nuevoCliente);
};

// Función para eliminar un cliente
export const eliminarCliente = (id) => {
    const index = clientesData.findIndex(cliente => cliente.id === id);
    if (index !== -1) {
        clientesData.splice(index, 1);
    }
};

// Función para agregar una película
export const agregarPelicula = (nombre, genero, duracion, inventario) => {
    const id = peliculasData.length + 1;
    const nuevaPelicula = { id, nombre, genero, duracion, inventario };
    peliculasData.push(nuevaPelicula);
};

// Función para eliminar una película
export const eliminarPelicula = (id) => {
    const index = peliculasData.findIndex(pelicula => pelicula.id === id);
    if (index !== -1) {
        peliculasData.splice(index, 1);
    }
};

// Función para agregar una renta
export const agregarRenta = (idPelicula, fechaRenta, diasRenta) => {
    const id = rentasData.length + 1;
    const nuevaRenta = { id, idPelicula, fechaRenta, diasRenta };
    rentasData.push(nuevaRenta);
};

// Función para eliminar una renta
export const eliminarRenta = (id) => {
    const index = rentasData.findIndex(renta => renta.id === id);
    if (index !== -1) {
        rentasData.splice(index, 1);
    }
};
