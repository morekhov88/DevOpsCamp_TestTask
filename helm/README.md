## Структура проекта пакетного менеджера HELM
* templates/
    * deployment.yaml
    * service.yaml
* Chart.yaml
* values.yaml

## Описание

### templates/deployment.yaml
Базовый манифест для создания Kubernetes deployment

### templates/services.yaml
Файл создающий сервис ClusterIP

### Chart.yaml
Файл содержащий информацию о чарте

### values.yaml
Файл содержащий значения конфигураций по умолчанию
