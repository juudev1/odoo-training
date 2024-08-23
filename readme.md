# Entrenamiento Odoo

# Guía para cargar modulos

## 1. Clonar el repositorio

```bash
git clone git@github.com:juudev1/odoo-training.git
```

## 2. Ubicarse en la carpeta del repositorio

```bash
cd odoo-training
```

## 3. Crear rama con tu nombre siguiendo la convención `nombre/apellido`

```bash
git checkout -b juan/perez
```

## 4. Crear un módulo

```bash
./odoo-bin scaffold my_module
```

Modifica tu módulo según tus necesidades.

## 5. Cargo el módulo en el repositorio

```bash
git add .
git commit -m "Agrego módulo my_module"
git push origin juan/perez
```
