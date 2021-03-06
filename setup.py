from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
  long_description = f.read()
        
setup(
  name = 'fexplorer',         # How you named your package folder (MyLib)
  packages = find_packages(include=['fexplorer', 'fexplorer.*']) ,   # Chose the same as "name"
  version = '0.0.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Simple file explorer made with python',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'aysilsimgekaracan',                   # Type in your name
  author_email = 'aysilsimge@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/aysilsimgekaracan/fexplorer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/aysilsimgekaracan/fexplorer/archive/refs/tags/v_0_0_4.tar.gz',    # I explain this later on
  keywords = ['CLI', 'FILE EXPLORER', 'EXPLORER'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pick',
      ],
  classifiers=[
    'Development Status :: 2 - Pre-Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Environment :: Console',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.9',
    'Topic :: Desktop Environment :: File Managers'
  ],
  entry_points= {
        'console_scripts': ['fexplorer=fexplorer.__main__:main']
    }
)