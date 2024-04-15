import React, { useState } from 'react';
import { clientesData } from '../data';
import { agregarCliente, eliminarCliente } from '../crudFunctions';
import './CRUDClientes.css';

const CRUDClientes = () => {
  const [nombre, setNombre] = useState('');
  const [apellidoPaterno, setApellidoPaterno] = useState('');
  const [apellidoMaterno, setApellidoMaterno] = useState('');
  const [email, setEmail] = useState('');
  const [clienteEditando, setClienteEditando] = useState(null);
  const [clientes, setClientes] = useState(clientesData);
  const [contadorId, setContadorId] = useState(clientesData.length > 0 ? clientesData.length + 1 : 1); // Inicializa el contador de id

  const handleAgregarEditarCliente = () => {
    if (clienteEditando !== null) {
      // Editar cliente existente
      const clientesActualizados = clientes.map(cliente => {
        if (cliente.id === clienteEditando) {
          return {
            ...cliente,
            nombre,
            apellidoPaterno,
            apellidoMaterno,
            email
          };
        }
        return cliente;
      });
      setClientes(clientesActualizados);
      setNombre('');
      setApellidoPaterno('');
      setApellidoMaterno('');
      setEmail('');
      setClienteEditando(null);
    } else {
      // Agregar nuevo cliente
      setClientes([...clientes, { id: contadorId, nombre, apellidoPaterno, apellidoMaterno, email }]);
      setContadorId(prevId => prevId + 1); // Incrementa el contador de id
      setNombre('');
      setApellidoPaterno('');
      setApellidoMaterno('');
      setEmail('');
    }
  };

  const handleSeleccionarCliente = (cliente) => {
    setClienteEditando(cliente.id);
    setNombre(cliente.nombre);
    setApellidoPaterno(cliente.apellidoPaterno);
    setApellidoMaterno(cliente.apellidoMaterno);
    setEmail(cliente.email);
  };

  const handleEliminarCliente = (id) => {
    if (clienteEditando === id) {
      return;
    }
    eliminarCliente(id);
    setClientes(clientes.filter(cliente => cliente.id !== id));
  };

  return (
    <div className="crud-clientes-container">
      <h2>CRUD de Clientes</h2>
      <div className="crud-clientes-form">
        <h3>{clienteEditando ? 'Editar Cliente' : 'Agregar Cliente'}</h3>
        <input type="text" placeholder="Nombre" value={nombre} onChange={(e) => setNombre(e.target.value)} />
        <input type="text" placeholder="Apellido Paterno" value={apellidoPaterno} onChange={(e) => setApellidoPaterno(e.target.value)} />
        <input type="text" placeholder="Apellido Materno" value={apellidoMaterno} onChange={(e) => setApellidoMaterno(e.target.value)} />
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
        <button onClick={handleAgregarEditarCliente}>{clienteEditando ? 'Editar Cliente' : 'Agregar Cliente'}</button>
      </div>
      <div>
        <h3>Lista de Clientes</h3>
        <ul className="crud-clientes-list">
          {clientes.map(cliente => (
            <li key={cliente.id} className="crud-clientes-item">
              {cliente.nombre} {cliente.apellidoPaterno} {cliente.apellidoMaterno} - {cliente.email}
              <button onClick={() => handleSeleccionarCliente(cliente)}>Editar</button>
              <button onClick={() => handleEliminarCliente(cliente.id)} disabled={clienteEditando === cliente.id}>Eliminar</button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default CRUDClientes;