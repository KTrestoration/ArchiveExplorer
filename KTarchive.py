from cloudmesh.common.Shell import Shell
import os

class KTclass:
    def __init__(self):
        pass


    @staticmethod
    def download_archive():
        # first check to see if ruby is installed

        import subprocess


        try:
            r = Shell.run('ruby -v')
            print(f'ruby version is {r}')
        except subprocess.CalledProcessError:
            print('uh oh ! ruby not installed')
            return False

        try:
            r = Shell.run('gem list -i "^wayback_machine_downloader$"')
        except subprocess.CalledProcessError:
            print('uh oh not downloaded')
            r = Shell.run('gem install wayback_machine_downloader')

        r = Shell.run('gem list -i "^wayback_machine_downloader$"')
        print(r)
        print(':)')

        print('checking to see if directory exists')
        if os.path.exists('./kidstube.com'):
            print('ok cool')
        else:
            print('making dir')
            Shell.mkdir('./kidstube.com')

        print('going to try using the gem now')

        missing = True

        while missing:
            cmd_str = 'wayback_machine_downloader kidstube.com --directory kidstube.com --all-timestamps --concurrency 4 --from 2008 --to 2016'
            completed_process = subprocess.run(cmd_str, shell=True)
            if not 'Failed to open TCP connection' in str(completed_process.stderr):
                print('Done')
                missing = False
            else:
                print('Missed some files. Redownloading...')

    @staticmethod
    def user_scraper():


        snapshot_dates_paths = []

        for path in (next(os.walk('./kidstube.com/'))[1]):

            look_in = os.path.join('./kidstube.com/', path)
            if 'users' in (next(os.walk(look_in))[1]):
                snapshot_dates_paths.append(os.path.abspath((os.path.join(look_in, 'users/'))))

        print(snapshot_dates_paths)
        new_usernames = []

        for full_path in snapshot_dates_paths:
            for path in (next(os.walk(full_path))[1]):
                new_usernames.append(os.path.basename(path))

        print(new_usernames)
        print(len(new_usernames))



