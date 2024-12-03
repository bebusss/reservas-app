from flask import Flask, render_template, request, jsonify
from connection import obtener_conexion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/pedidos', methods=['GET', 'POST'])
def pedidos():
    if request.method == 'GET':
        return render_template('pedidos.html')

    if request.method == 'POST':
        data = request.form
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO Pedidos (UsuarioID, Estado, Total)
            VALUES (?, 'En preparación', ?);
        """
        cursor.execute(query, (data['UsuarioID'], data['Total']))
        conexion.commit()
        conexion.close()
        return jsonify({'message': 'Pedido registrado con éxito'}), 201

@app.route('/reservas', methods=['GET', 'POST'])
def reservas():
    if request.method == 'GET':
        return render_template('reservas.html')

    if request.method == 'POST':
        data = request.form
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = """
            INSERT INTO Reservas (UsuarioID, FechaReserva, HoraReserva, NumeroPersonas, Estado)
            VALUES (?, ?, ?, ?, 'Pendiente');
        """
        cursor.execute(query, (data['UsuarioID'], data['FechaReserva'], data['HoraReserva'], data['NumeroPersonas']))
        conexion.commit()
        conexion.close()
        return jsonify({'message': 'Reserva registrada con éxito'}), 201

if __name__ == '__main__':
    app.run(debug=True)
