from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configuración de la conexión
DB_CONFIG = {
    'dbname': 'alimentos',
    'user': 'postgres',
    'password': '1234567',
    'host': 'localhost',  # Cambia si tu servidor está en otro lugar
    'port': 5432
}

# Conexión a la base de datos
def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Error conectando a la base de datos:", e)
        return None

@app.route('/nombrealimentos', methods=['GET'])
def get_all_nombrealimentos():
    """Obtiene todos los alimentos."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""SELECT "Alimento" FROM public."Datos_alimentos";""")
            alimentos = cursor.fetchall()
            return jsonify(alimentos), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

@app.route('/alimentos', methods=['GET'])
def get_all_alimentos():
    """Obtiene todos los alimentos."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""SELECT * FROM public."Datos_alimentos";""")
            alimentos = cursor.fetchall()
            return jsonify(alimentos), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

@app.route('/alimentos/categoria/<string:nombre>', methods=['GET'])
def get_categoria_by_nombre(nombre):
    """Obtiene todos los alimentos de una misma categoría."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query = """SELECT * FROM public."Datos_alimentos" WHERE "Categoria" = (SELECT "Categoria" FROM public."Datos_alimentos" WHERE "Alimento" = %s) AND "Alimento" != %s;"""
            cursor.execute(query, (nombre,nombre))
            alimentos = cursor.fetchall()
            if alimentos:
                return jsonify(alimentos), 200
            else:
                return jsonify({"error": "No se encontraron alimentos dentro de la misma categoría"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

# @app.route('/alimentos/categoria/<string:categoria>', methods=['GET'])
# def get_alimentos_by_categoria(categoria):
#     """Obtiene todos los alimentos de una misma categoría."""
#     conn = connect_to_db()
#     if conn:
#         try:
#             cursor = conn.cursor(cursor_factory=RealDictCursor)
#             query = """SELECT * FROM public."Datos_alimentos" WHERE "Categoria" = %s;"""
#             cursor.execute(query, (categoria,))
#             alimentos = cursor.fetchall()
#             if alimentos:
#                 return jsonify(alimentos), 200
#             else:
#                 return jsonify({"error": "No se encontraron alimentos en esta categoría"}), 404
#         except Exception as e:
#             return jsonify({"error": str(e)}), 500
#         finally:
#             conn.close()
#     else:
#         return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

@app.route('/alimentos/<int:id>', methods=['GET'])
def get_alimento_by_id(id):
    """Obtiene un alimento por su ID."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""SELECT * FROM public."Datos_alimentos" WHERE id = %s;""", (id,))
            alimento = cursor.fetchone()
            if alimento:
                return jsonify(alimento), 200
            else:
                return jsonify({"error": "Alimento no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()

@app.route('/alimentos/<string:nombre>', methods=['GET'])
def get_info_alimento_by_nombre(nombre):
    """Obtiene datos de un alimento por su nombre."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            cursor.execute("""SELECT * FROM public."Datos_alimentos" WHERE "Alimento" = %s;""", (nombre,))
            alimento = cursor.fetchone()
            if alimento:
                return jsonify(alimento), 200
            else:
                return jsonify({"error": "Alimento no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()

@app.route('/alimentos', methods=['POST'])
def create_alimento():
    """Crea un nuevo alimento."""
    data = request.json
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            INSERT INTO public."Datos_alimentos" ("Alimento", "Categoria", "Cantidad", "Unidad", "Peso_bruto", "Peso_neto", "Energia", "Proteinas", "Lipidos", "Carbohidratos")
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                data['Alimento'], data['Categoria'], data['Cantidad'], data['Unidad'], 
                data['Peso_bruto'], data['Peso_neto'], data['Energia'], 
                data['Proteinas'], data['Lipidos'], data['Carbohidratos']
            ))
            conn.commit()
            new_id = cursor.fetchone()[0]
            return jsonify({"message": "Alimento creado", "id": new_id}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

@app.route('/alimentos/<int:id>', methods=['PUT'])
def update_alimento(id):
    """Actualiza un alimento existente."""
    data = request.json
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
            UPDATE public."Datos_alimentos"
            SET "Alimento" = %s, "Categoria" = %s, "Cantidad" = %s, "Unidad" = %s, 
                "Peso_bruto" = %s, "Peso_neto" = %s, "Energia" = %s, 
                "Proteinas" = %s, "Lipidos" = %s, "Carbohidratos" = %s
            WHERE id = %s;
            """
            cursor.execute(query, (
                data['Alimento'], data['Categoria'], data['Cantidad'], data['Unidad'], 
                data['Peso_bruto'], data['Peso_neto'], data['Energia'], 
                data['Proteinas'], data['Lipidos'], data['Carbohidratos'], id
            ))
            conn.commit()
            if cursor.rowcount > 0:
                return jsonify({"message": "Alimento actualizado"}), 200
            else:
                return jsonify({"error": "Alimento no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

@app.route('/alimentos/<int:id>', methods=['DELETE'])
def delete_alimento(id):
    """Elimina un alimento."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """DELETE FROM public."Datos_alimentos" WHERE id = %s;"""
            cursor.execute(query, (id,))
            conn.commit()
            if cursor.rowcount > 0:
                return jsonify({"message": "Alimento eliminado"}), 200
            else:
                return jsonify({"error": "Alimento no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        finally:
            conn.close()
    else:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
