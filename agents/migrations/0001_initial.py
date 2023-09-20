# Generated by Django 4.0.4 on 2022-06-17 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentBuyCryptoModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('agentName', models.CharField(max_length=100)),
                ('agentemail', models.CharField(max_length=100)),
                ('currencyname', models.CharField(max_length=100)),
                ('currentprice', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('payableammount', models.FloatField()),
                ('cardnumber', models.CharField(max_length=100)),
                ('nameoncard', models.CharField(max_length=100)),
                ('cardexpiry', models.CharField(max_length=100)),
                ('cvv', models.IntegerField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'AgentBuyedTransactions',
            },
        ),
        migrations.CreateModel(
            name='BitAgentRegisterModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('pswd', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('pan', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('cryptcurrency', models.CharField(max_length=100)),
                ('status', models.CharField(default='waiting', max_length=100)),
                ('authkey', models.CharField(default='waiting', max_length=100)),
                ('cdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'agentregister',
            },
        ),
        migrations.CreateModel(
            name='AgentHadCrypto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('currencyName', models.CharField(max_length=100)),
                ('useremail', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'agentscryptoquantity',
                'unique_together': {('currencyName', 'useremail')},
            },
        ),
    ]