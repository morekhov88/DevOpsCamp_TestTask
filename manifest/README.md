## Описание

Манифест содержит в себе три блока:
* Создание неймспейса
* Код для запуска приложения в Kubernetes в отдельном неймспейсе в виде Deployment с 3 репликами. Реализующий readiness- и liveness- пробы и подставляющий уникальный идентификатор пода в кластере, в котором запущено приложение
* Создание сервиса ClusterIP в отдельном неймспейсе
## Использование

Команда для запуска манифеста
```bash
kubectl apply -f deployment_manifest.yaml
```

ВНИМАНИЕ! Для взаимодействия с подами и сервисом необходимо добавлять название неймспейса `-n=my-space`

