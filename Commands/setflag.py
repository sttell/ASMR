from Core.JSRL.jsloader import load_settings, save_settings
import subprocess as sbp
import os


'''
                        sf -- Set Flags.
This command allows you to set options that are passed to the compiler when executing
bundle files. Options are checked for compatibility with the compiler
by running test files in three configurations: C, Assembler, C + Assembler.

To set the flags, enter: asmr sf|setf|setflag [opts]

Ex: asmr sf -no-pie -fopenmp -o3
    asmr setflag -no-pie
    asmr setf -o3
'''


def run(args, opts):
    settings = load_settings() # load settings

    if opts:
        for opt in opts:

            # TEST NEW FLAG
            compiler = settings['compiler']
            testc_file_path = os.path.abspath('./Tests/test.c')
            tests_file_path = os.path.abspath('./Tests/test.s')
            mtestc = os.path.abspath('./Tests/mul_test.c')
            mtests = os.path.abspath('./Tests/mul_test.s')
            command1 = f'{compiler} {opt} {testc_file_path}'
            command2 = f'{compiler} {opt} {tests_file_path}'
            command3 = f'{compiler} {opt} {mtestc} {mtests}'
            
            res1 = sbp.call(command1, shell=True)
            res2 = sbp.call(command2, shell=True)
            res3 = sbp.call(command3, shell=True)

            if str(res1) == 1:
                print('Возникли проблемы. Компилятор не может обрабатывать файлы С.')
                return 1
            elif str(res2) == 1:
                print('Возникли проблемы. Компилятор не может обрабатывать файлы Assembler.')
                return 1
            elif str(res3) == 1:
                print('Возникли проблемы. Компилятор не может обрабатывать файлы Assembler + C.')
                return 1
            else:
                pass

        # Update flags
        settings['compiler-flags'] = opts
        save_settings(settings)
        print('Опции успешно установлены.')
    else:
        # reset flags
        settings['compiler-flags'] = []
        save_settings(settings)
        print('Опции передаваемые компиляторы очищены.')    


def get_help(args, opts):
    print('''\n                        sf -- Set Flags.
Данная команда позволяет задать опции передаваемые компилятору при исполнении
файлов связок. Опции проходят проверку на совместимость с компилятором
с помощью запуска тестовых файлов в трех конфигурациях: С, Assembler, C + Assembler.

Для того чтобы задать флаги необходимо ввести: asmr sf|setf|setflag [opts]

Ex: asmr sf -no-pie -fopenmp -o3
    asmr setflag -no-pie
    asmr setf -o3


''')