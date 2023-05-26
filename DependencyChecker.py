import subprocess
import pip

## DependencyChecker.py: A script that checks for and updates project dependencies can 
  # help keep the project up-to-date with the latest library versions.

def check_dependency_updates():
    # Get the list of installed packages and their versions
    installed_packages = pip.get_installed_distributions()
    packages_to_update = []

    for package in installed_packages:
        package_name = package.project_name
        current_version = package.version

        # Check if there is a newer version available for the package
        try:
            latest_version = subprocess.check_output(['pip', 'install', '--no-cache-dir', '--upgrade', package_name])
            latest_version = latest_version.decode('utf-8').strip()
            if latest_version != current_version:
                packages_to_update.append((package_name, current_version, latest_version))
        except subprocess.CalledProcessError:
            # Failed to get the latest version, skip this package
            continue

    # Print the packages that need to be updated
    if packages_to_update:
        print("Packages to update:")
        for package in packages_to_update:
            package_name, current_version, latest_version = package
            print(f"{package_name}: {current_version} -> {latest_version}")
    else:
        print("All packages are up-to-date.")


if __name__ == '__main__':
    check_dependency_updates()
