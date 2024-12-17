from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import mysql.connector
<<<<<<< HEAD
from .validation_functions import validate_first_name, validate_middle_name, validate_last_name, validate_birthday, validate_age, validate_contact_number, validate_email
=======
from .validation_functions import validate_first_name, validate_middle_name, validate_last_name, validate_birthday, validate_age, validate_contact_number, validate_email, validate_username, validate_password
>>>>>>> c0d931b (Initial commit)

crud_blueprint = Blueprint('crud', __name__, template_folder='templates')

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'users_db',
    'auth_plugin': 'mysql_native_password'
}

@crud_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' not in session:
        flash('Please log in first.', 'warning')
        return redirect(url_for('login.index'))
    
<<<<<<< HEAD
    if request.method == 'POST':
        firstname = request.form['firstname'].strip()
        middlename = request.form['middlename'].strip()
        lastname = request.form['lastname'].strip()
        birthday = request.form['birthday'].strip()
        age = request.form['age'].strip()
        contact_number = request.form['contact_number'].strip()
        email = request.form['email'].strip()
        # username = request.form['username']
        # password = request.form['password']

        # Validate fields and store the error messages
        first_name_error = validate_first_name(firstname)
        middle_name_error = validate_middle_name(middlename)
        last_name_error = validate_last_name(lastname)
        birthday_error = validate_birthday(birthday, age)
        age_error = validate_age(age, birthday)
        contact_number_error = validate_contact_number(contact_number)
        email_error = validate_email(email)

        # If there are validation errors, pass them to the template
        if first_name_error or middle_name_error or last_name_error or birthday_error or age_error or contact_number_error or email_error:
            return render_template('create.html', 
                                first_name_error=first_name_error,
                                middle_name_error=middle_name_error,
                                last_name_error=last_name_error,
                                birthday_error=birthday_error,
                                age_error=age_error,
                                contact_number_error=contact_number_error,
                                email_error=email_error,
                                firstname=firstname,
                                middlename=middlename,
                                lastname=lastname,
                                birthday=birthday,
                                age=age,
                                contact_number=contact_number,
                                email=email,
                                )

        # If no validation errors, insert data into the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        try:
            cursor.execute('INSERT INTO users_info (firstname, middlename, lastname, birthday, age, contact_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (firstname, middlename, lastname, birthday, age, contact_number, email))
            conn.commit()
            return '''
                <script>
                    alert('User added successfully!');
                    window.location.href = "{}";
                </script>
                '''.format(url_for('account.index'))
            # flash('User added successfully!', 'success')
            # return redirect(url_for('account.index'))  # Redirect to another page after successful addition
        except Exception as e:
            flash(f"Error adding user: {e}", 'danger')
            return render_template('create.html')
        finally:
            cursor.close()
            conn.close()
    else:
        return render_template('create.html')


    
=======
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    try:
        if request.method == 'POST':
            firstname = request.form['firstname'].strip()
            middlename = request.form['middlename'].strip()
            lastname = request.form['lastname'].strip()
            birthday = request.form['birthday'].strip()
            age = request.form['age'].strip()
            contact_number = request.form['contact_number'].strip()
            email = request.form['email'].strip()
            username = request.form['username'].strip()
            password = request.form['password'].strip()

            # Validate fields and store the error messages
            first_name_error = validate_first_name(firstname)
            middle_name_error = validate_middle_name(middlename)
            last_name_error = validate_last_name(lastname)
            birthday_error = validate_birthday(birthday, age)
            age_error = validate_age(age, birthday)
            contact_number_error = validate_contact_number(contact_number)
            email_error = validate_email(email)
            username_error = validate_username(username)
            password_error = validate_password(password)

            # If there are validation errors, pass them to the template
            if first_name_error or middle_name_error or last_name_error or birthday_error or age_error or contact_number_error or email_error or username_error or password_error:
                return render_template('create.html', 
                                    first_name_error=first_name_error,
                                    middle_name_error=middle_name_error,
                                    last_name_error=last_name_error,
                                    birthday_error=birthday_error,
                                    age_error=age_error,
                                    contact_number_error=contact_number_error,
                                    email_error=email_error,
                                    username_error=username_error,
                                    password_error=password_error,
                                    firstname=firstname,
                                    middlename=middlename,
                                    lastname=lastname,
                                    birthday=birthday,
                                    age=age,
                                    contact_number=contact_number,
                                    email=email,
                                    username=username,
                                    password=password
                                    )

            # Check if the username already exists
            cursor.execute('SELECT * FROM users_info WHERE username = %s', (username,))
            existing_username = cursor.fetchone()
            
            # Check if the email already exists
            cursor.execute('SELECT * FROM users_info WHERE email = %s', (email,))
            existing_email = cursor.fetchone()

            if existing_username:
                username_error = 'Username already exists. Please choose another one.'
            if existing_email:
                email_error = 'Email already exists. Please choose another one.'
            
            # If either username or email exists, render template with errors
            if existing_username or existing_email:
                return render_template('create.html', 
                                    firstname=firstname,
                                    middlename=middlename,
                                    lastname=lastname,
                                    birthday=birthday,
                                    age=age,
                                    contact_number=contact_number,
                                    email=email,
                                    username=username,
                                    password=password,
                                    username_error=username_error,
                                    email_error=email_error
                                    )

            # Insert the new user if no existing user found
            cursor.execute('INSERT INTO users_info (firstname, middlename, lastname, birthday, age, contact_number, email, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                        (firstname, middlename, lastname, birthday, age, contact_number, email, username, password))
            conn.commit()

            flash('User added successfully!', 'success')
            return redirect(url_for('account.index'))  # Redirect after successful addition

    except Exception as e:
        flash(f"Error occurred: {e}", 'danger')
        return render_template('create.html')

    cursor.close()
    conn.close()

    return render_template('create.html')

>>>>>>> c0d931b (Initial commit)
@crud_blueprint.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    try:
        cursor.execute('DELETE FROM users_info WHERE id=%s', (id,))
        conn.commit()
        return redirect(url_for('account.index'))
    except mysql.connector.Error as e:
        return f"Deleting data failed! Error: {str(e)}"
    finally:
        cursor.close()
        conn.close() 