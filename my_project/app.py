from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'


user_data = {
    "name": "Иван Иванов",
    "email": "ivan@example.com",
    "password": "password123"
}


@app.route('/')
def home():
    return render_template('profile.html', user=user_data)


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Обновляем данные пользователя
        user_data['name'] = name
        user_data['email'] = email
        user_data['password'] = password

        flash('Профиль успешно обновлён!', 'success')
        return redirect(url_for('home'))

    return render_template('edit_profile.html', user=user_data)


if __name__ == '__main__':
    app.run(debug=True)
