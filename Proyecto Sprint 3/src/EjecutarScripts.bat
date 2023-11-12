echo. ##############TEST PATH #############
cd ./Tests
python -m pytest test_001.py test_002.py test_003.py --html=../Results/CastillaCesia.html --self-contained-html
pause