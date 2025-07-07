## POSCARs2Feat

(

`path`: <class 'str'> = ./

`verbose`: <class 'int'> = 0

`args`: <class 'inspect._empty'>

`kwargs`: <class 'inspect._empty'>

)


    Read and convert a folder of POSCAR files from given path into arrays of atoms, coordinates, cell vectors, etc.
    

## append

(

`batch_structures`: <class 'inspect._empty'>

`strict`: <class 'bool'> = True

)


        Append information of another BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## cartesian2direct

(

)

 Convert Cartesian coordinates to Direct coordinates. Only work in 'L' Mode. 

## contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain all given elements.
        

## contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain any of given elements.
        

## contain_only_in

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that only contain given elements.
        

## direct2cartesian

(

)

 Convert Direct coordinates to Cartesian coordinates. Only work in 'L' Mode. 

## elem_distribution

(

`count_for`: typing.Literal['Atom', 'Structure'] = Structure

)


        return a Dict[str, int] of {element: frequency} that shows the distribution of elements in BatchStructures.

        Parameters:
            count_for: 'Atom' or 'Structure', count element frequency by each atom in structures or each structure.
        

## extend

(

`batch_structures_list`: typing.Sequence

`strict`: <class 'bool'> = True

)


        Extend a list of BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures_list: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## generate_atom_list

(

`force_update`: <class 'bool'> = False

)


        Generate an attribute self.Atom_list (List[str]) which is the atom lists in order of the atomic coordinates sequence.

        Parameters:
            force_update: bool. if False, Atom_list would not be updated when it's not None.
        

## generate_atomic_number_list

(

`force_update`: <class 'bool'> = False

)


        Generate attribute self.Atomic_number_list (List[int]) which is the atomic number lists in order of the sequence of atom coordinates.

        Parameters:
            force_update: bool. if False, Atomic_number_list would not be updated when it's not None.
        

## generate_dist_mat

(

`supercell_indices`: <class 'inspect._empty'> = [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00]]

)


        Parameters:
            supercell_indices: NDArray[n_supercell, 3], the indices of supercells that calculate distance.

        self.Dist_mat Format: List[Tensor[(n_prim_cells, n_atom, n_atom)]]
        

## load

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

`mode`: typing.Literal['w', 'a'] = w

)


        Load data from saved files.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.
            mode: the data load mode. 'W' for write or overwrite existing data from data in file; 'a' for appending data in file to existing data.

        Returns: None

        

## load_from_file

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

)


        The class method version for loading data from saved files.
        WARNING: It would overwrite the existing BatchStructure data. Use `self.load(..., mode='a')` to retain existing data.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.

        Returns: Self with loaded data.

        

## not_contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that Not contain all given elements at the same time.
        

## not_contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

`verbose`: <class 'int'> = 0

)


        Return a view of BatchStructures that Not contain any of given elements.
        

## para_read

(

`file_list`: typing.Optional[typing.List] = None

`output_coord_type`: <class 'str'> = cartesian

`n_core`: <class 'int'> = -1

`backend`: <class 'inspect._empty'> = loky

)


        Reading file in parallel.
        Parameters:
            file_list: list (or other Sequences), the list of selected files to be read. 'None' means read all files in the input path.
            output_coord_type: str, 'cartesian' or 'direct'. The coordination type of output atom coordination.
            n_core: int, the number of CPU cores used in reading files.
            backend: backend for parallelization in joblib. Options: 'loky', 'threading', 'multiprocessing'.
        

## read

(

`file_list`: typing.Optional[typing.List] = None

`output_coord_type`: <class 'str'> = cartesian

)



        Args:
            file_list: list (or other Sequences), the list of selected files to be read. 'None' means read all files in the input path.
            output_coord_type: str, 'cartesian' or 'direct'. The coordination type of output atom coordination.

        Returns:

        

## rearrange

(

`indices`: typing.List[int]

)


        Rearrange the order of samples by given indices.
        Args:
            indices: indices of sample orders.

        Returns: None

        

## remove

(

`key`: int | str | slice

)


        Remove the data of given `key` in-place.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: None

        

## remove_copy

(

`key`: int | str | slice

)


        Remove the data of given `key` in a copy of self and return. The original data is not affected.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: copy of

        

## revise

(

`index`: int | str

`rev_Sample_ids`: None | str = None

`rev_Cells`: None | numpy.ndarray = None

`rev_Elements`: typing.Optional[typing.List[str]] = None

`rev_Numbers`: typing.Optional[typing.List[int]] = None

`rev_Coords_type`: typing.Optional[typing.Literal['C', 'D']] = None

`rev_Coords`: None | numpy.ndarray = None

`rev_Fixed`: None | numpy.ndarray = None

`rev_Energies`: None | float = None

`rev_Forces`: None | numpy.ndarray = None

`rev_Labels`: typing.Any | None = None

)


        Revising data of given `index`. None is for not changing.
        Args:
            index:
            rev_Sample_ids:
            rev_Cells:
            rev_Elements:
            rev_Numbers:
            rev_Coords_type:
            rev_Coords:
            rev_Fixed:
            rev_Energies:
            rev_Forces:
            rev_Labels:

        

## save

(

`path`: <class 'str'>

`mode`: typing.Literal['w', 'a'] = w

)


        Saving this BatchStructures to a numpy memory-mapping file.
        Each attribute in BatchStructures will be saved in the numpy memmap file with the same name.
        Additionally, file 'head' will record the information which is data type & shape of all attributes, and record which attributes are `None`.

        Args:
            path: the saving directory.
            mode: if 'w', create or overwrite the existing file for reading and writing. If 'a', data will append to the existing file.

        Returns: None

        

## select_by_element_number

(

`element_number_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that element number between element_number_range.
        

## select_by_energies

(

`energy_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that Energies between energy_range.
        

## select_by_prop

(

`prop`: <class 'str'>

`prop_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that given properties of BatchStructures between prop_range.
        The given properties must be comparable.

        Args:
            prop: an attribute name of self e.g., "Number", "Energies"
            prop_range: Tuple[float, float], range of prop to select. It is a left closed right open interval.

        Returns:
            BatchStructures which is a view of self
        

## select_by_sample_id

(

`pattern`: <class 'str'>

)


        Return a view of BatchStructures in which sample id could match the given pattern.
        Regular expressions are supported.
        For non-string sample id, str(*) would be applied first to convert id into string.
        Args:
            pattern: the (regular expressions) pattern to match sample ids in self.

        Returns: BatchStructures

        

## set_Energies

(

`val`: typing.Union[typing.Sequence, typing.Dict]

)


        Set or reset self.Energies from input `val`.
        Args:
            val: the input values to set self.Energies
                if Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## set_Forces

(

`val`: typing.Union[typing.Sequence[numpy.ndarray], typing.Dict[str, numpy.ndarray]]

)


        Set or reset self.Forces from `val`.
        Args:
            val: the input values to set self.Forces
                if Dict, val: {sample_id: forces, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns:

        

## set_Labels

(

`val`: typing.Union[typing.Sequence, typing.Dict, numpy.ndarray]

)


        Set or reset self.Labels from input `val`.
        Args:
            val: the input values of self.Labels to set.
            If Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## show

(

`number`: int | slice

)


        Show the information of samples in given slice `number`.
        Args:
            number: the slice of samples to show.

        Returns: None.

        

## shuffle

(

`seed`: <class 'int'> = None

)


        Shuffle the samples with given random seed.
        Args:
            seed: random seed.

        Returns: None

        

## sort_split_by_natoms

(

`labels`: typing.Union[typing.Dict, typing.List, NoneType] = None

`split_ratio`: <class 'float'> = 0.2

`n_core`: <class 'int'> = 1

`verbose`: <class 'int'> = 0

)


        Rearrange samples with different atom number into List[np.array] that list of NDArrays with the same atom number.
        Only work in 'L' Mode.

        Parameters:
            labels: Dict[id, label]|List[label]|None, the labels of samples. If labels is a List, it must have the same order as self.Sample_ids. If None, labels would be set to self.Labels.
            split_ratio: float between 0 and 1, the ratio of validation set.
            n_core:
            verbose: control the verboseness of output

        Returns:
            training_batches, val_batches: List_1[List_2[NDArray]]. List_1 is of diff. n_atom cells, List_2 is of (Cell, Atomic_number_list, Atom_coords)
            training_labels, val_labels: List[NDArray]. List is of diff. n_atom cells, NDArray is label.
            training_args, val_args: List[NDArray]. List is of diff. n_atom cells, NDArray is the indices of samples in self.Samp_id.
        

## write2text

(

`output_path`: <class 'str'> = ./

`indices`: typing.Union[int, str, typing.List[int], typing.Tuple[int, int], NoneType] = None

`file_format`: typing.Literal['POSCAR', 'cif', 'xyz', 'xyz_forces'] = POSCAR

`file_name_list`: typing.Union[str, typing.Sequence[str], NoneType] = None

`n_core`: <class 'int'> = -1

)


        Write selected structures to text files in given format.
        Args:
            indices: the selection indices of `self`. If Tuple, structures between `indices[0]` and `indices[1]` will be selected.
            file_format: the format of written files.
                'POSCAR': vasp POSCAR format
                'cif': crystallographic information file
                'xyz': ext-xyz file that only contains atomic positions
                'xyz_forces': ext-xyz file that contains atomic positions and forces
            output_path: the directory of output file.
            file_name_list: the list of file names. If None, it would be set to `Sample_ids`.
            n_core: number of CPU cores to write in parallel. `-1` for all available CPU cores.

        Returns: None

        

## OUTCAR2Feat

(

`path`: <class 'str'>

`verbose`: <class 'int'> = 1

)


    Read atoms, coordinates, atom numbers, energies and force in OUTCARs from given path.
    Notes: Because OUTCAR does not store any information of fixed atom (selective dynamics), all atoms would be set to FREE!!

    Parameters:
        path: str, the path of batched OUTCAR-like files. The Sample ids would be labeled as its file names.
    

## append

(

`batch_structures`: <class 'inspect._empty'>

`strict`: <class 'bool'> = True

)


        Append information of another BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## cartesian2direct

(

)

 Convert Cartesian coordinates to Direct coordinates. Only work in 'L' Mode. 

## contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain all given elements.
        

## contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain any of given elements.
        

## contain_only_in

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that only contain given elements.
        

## direct2cartesian

(

)

 Convert Direct coordinates to Cartesian coordinates. Only work in 'L' Mode. 

## elem_distribution

(

`count_for`: typing.Literal['Atom', 'Structure'] = Structure

)


        return a Dict[str, int] of {element: frequency} that shows the distribution of elements in BatchStructures.

        Parameters:
            count_for: 'Atom' or 'Structure', count element frequency by each atom in structures or each structure.
        

## extend

(

`batch_structures_list`: typing.Sequence

`strict`: <class 'bool'> = True

)


        Extend a list of BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures_list: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## generate_atom_list

(

`force_update`: <class 'bool'> = False

)


        Generate an attribute self.Atom_list (List[str]) which is the atom lists in order of the atomic coordinates sequence.

        Parameters:
            force_update: bool. if False, Atom_list would not be updated when it's not None.
        

## generate_atomic_number_list

(

`force_update`: <class 'bool'> = False

)


        Generate attribute self.Atomic_number_list (List[int]) which is the atomic number lists in order of the sequence of atom coordinates.

        Parameters:
            force_update: bool. if False, Atomic_number_list would not be updated when it's not None.
        

## generate_dist_mat

(

`supercell_indices`: <class 'inspect._empty'> = [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00]]

)


        Parameters:
            supercell_indices: NDArray[n_supercell, 3], the indices of supercells that calculate distance.

        self.Dist_mat Format: List[Tensor[(n_prim_cells, n_atom, n_atom)]]
        

## load

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

`mode`: typing.Literal['w', 'a'] = w

)


        Load data from saved files.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.
            mode: the data load mode. 'W' for write or overwrite existing data from data in file; 'a' for appending data in file to existing data.

        Returns: None

        

## load_from_file

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

)


        The class method version for loading data from saved files.
        WARNING: It would overwrite the existing BatchStructure data. Use `self.load(..., mode='a')` to retain existing data.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.

        Returns: Self with loaded data.

        

## not_contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that Not contain all given elements at the same time.
        

## not_contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

`verbose`: <class 'int'> = 0

)


        Return a view of BatchStructures that Not contain any of given elements.
        

## read

(

`file_list`: typing.Optional[typing.List[str]] = None

`n_core`: <class 'int'> = -1

`backend`: <class 'str'> = loky

)


        Parameters:
            file_list: List[str], the list of files to read. Default for all files under given path.
            n_core: int, the number of CPU cores used in reading files.
            backend: backend for parallelization in joblib. Options: 'loky', 'threading', 'multiprocessing'.

        Return: None
        Update the attribute self.data.
        

## rearrange

(

`indices`: typing.List[int]

)


        Rearrange the order of samples by given indices.
        Args:
            indices: indices of sample orders.

        Returns: None

        

## remove

(

`key`: int | str | slice

)


        Remove the data of given `key` in-place.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: None

        

## remove_copy

(

`key`: int | str | slice

)


        Remove the data of given `key` in a copy of self and return. The original data is not affected.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: copy of

        

## revise

(

`index`: int | str

`rev_Sample_ids`: None | str = None

`rev_Cells`: None | numpy.ndarray = None

`rev_Elements`: typing.Optional[typing.List[str]] = None

`rev_Numbers`: typing.Optional[typing.List[int]] = None

`rev_Coords_type`: typing.Optional[typing.Literal['C', 'D']] = None

`rev_Coords`: None | numpy.ndarray = None

`rev_Fixed`: None | numpy.ndarray = None

`rev_Energies`: None | float = None

`rev_Forces`: None | numpy.ndarray = None

`rev_Labels`: typing.Any | None = None

)


        Revising data of given `index`. None is for not changing.
        Args:
            index:
            rev_Sample_ids:
            rev_Cells:
            rev_Elements:
            rev_Numbers:
            rev_Coords_type:
            rev_Coords:
            rev_Fixed:
            rev_Energies:
            rev_Forces:
            rev_Labels:

        

## save

(

`path`: <class 'str'>

`mode`: typing.Literal['w', 'a'] = w

)


        Saving this BatchStructures to a numpy memory-mapping file.
        Each attribute in BatchStructures will be saved in the numpy memmap file with the same name.
        Additionally, file 'head' will record the information which is data type & shape of all attributes, and record which attributes are `None`.

        Args:
            path: the saving directory.
            mode: if 'w', create or overwrite the existing file for reading and writing. If 'a', data will append to the existing file.

        Returns: None

        

## select_by_element_number

(

`element_number_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that element number between element_number_range.
        

## select_by_energies

(

`energy_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that Energies between energy_range.
        

## select_by_prop

(

`prop`: <class 'str'>

`prop_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that given properties of BatchStructures between prop_range.
        The given properties must be comparable.

        Args:
            prop: an attribute name of self e.g., "Number", "Energies"
            prop_range: Tuple[float, float], range of prop to select. It is a left closed right open interval.

        Returns:
            BatchStructures which is a view of self
        

## select_by_sample_id

(

`pattern`: <class 'str'>

)


        Return a view of BatchStructures in which sample id could match the given pattern.
        Regular expressions are supported.
        For non-string sample id, str(*) would be applied first to convert id into string.
        Args:
            pattern: the (regular expressions) pattern to match sample ids in self.

        Returns: BatchStructures

        

## set_Energies

(

`val`: typing.Union[typing.Sequence, typing.Dict]

)


        Set or reset self.Energies from input `val`.
        Args:
            val: the input values to set self.Energies
                if Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## set_Forces

(

`val`: typing.Union[typing.Sequence[numpy.ndarray], typing.Dict[str, numpy.ndarray]]

)


        Set or reset self.Forces from `val`.
        Args:
            val: the input values to set self.Forces
                if Dict, val: {sample_id: forces, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns:

        

## set_Labels

(

`val`: typing.Union[typing.Sequence, typing.Dict, numpy.ndarray]

)


        Set or reset self.Labels from input `val`.
        Args:
            val: the input values of self.Labels to set.
            If Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## show

(

`number`: int | slice

)


        Show the information of samples in given slice `number`.
        Args:
            number: the slice of samples to show.

        Returns: None.

        

## shuffle

(

`seed`: <class 'int'> = None

)


        Shuffle the samples with given random seed.
        Args:
            seed: random seed.

        Returns: None

        

## sort_split_by_natoms

(

`labels`: typing.Union[typing.Dict, typing.List, NoneType] = None

`split_ratio`: <class 'float'> = 0.2

`n_core`: <class 'int'> = 1

`verbose`: <class 'int'> = 0

)


        Rearrange samples with different atom number into List[np.array] that list of NDArrays with the same atom number.
        Only work in 'L' Mode.

        Parameters:
            labels: Dict[id, label]|List[label]|None, the labels of samples. If labels is a List, it must have the same order as self.Sample_ids. If None, labels would be set to self.Labels.
            split_ratio: float between 0 and 1, the ratio of validation set.
            n_core:
            verbose: control the verboseness of output

        Returns:
            training_batches, val_batches: List_1[List_2[NDArray]]. List_1 is of diff. n_atom cells, List_2 is of (Cell, Atomic_number_list, Atom_coords)
            training_labels, val_labels: List[NDArray]. List is of diff. n_atom cells, NDArray is label.
            training_args, val_args: List[NDArray]. List is of diff. n_atom cells, NDArray is the indices of samples in self.Samp_id.
        

## write2text

(

`output_path`: <class 'str'> = ./

`indices`: typing.Union[int, str, typing.List[int], typing.Tuple[int, int], NoneType] = None

`file_format`: typing.Literal['POSCAR', 'cif', 'xyz', 'xyz_forces'] = POSCAR

`file_name_list`: typing.Union[str, typing.Sequence[str], NoneType] = None

`n_core`: <class 'int'> = -1

)


        Write selected structures to text files in given format.
        Args:
            indices: the selection indices of `self`. If Tuple, structures between `indices[0]` and `indices[1]` will be selected.
            file_format: the format of written files.
                'POSCAR': vasp POSCAR format
                'cif': crystallographic information file
                'xyz': ext-xyz file that only contains atomic positions
                'xyz_forces': ext-xyz file that contains atomic positions and forces
            output_path: the directory of output file.
            file_name_list: the list of file names. If None, it would be set to `Sample_ids`.
            n_core: number of CPU cores to write in parallel. `-1` for all available CPU cores.

        Returns: None

        

## ASETraj2Feat

(

`path`: <class 'str'>

`verbose`: <class 'int'> = 1

)


    read ASE files to BatchStructures.
    

## append

(

`batch_structures`: <class 'inspect._empty'>

`strict`: <class 'bool'> = True

)


        Append information of another BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## cartesian2direct

(

)

 Convert Cartesian coordinates to Direct coordinates. Only work in 'L' Mode. 

## contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain all given elements.
        

## contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain any of given elements.
        

## contain_only_in

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that only contain given elements.
        

## direct2cartesian

(

)

 Convert Direct coordinates to Cartesian coordinates. Only work in 'L' Mode. 

## elem_distribution

(

`count_for`: typing.Literal['Atom', 'Structure'] = Structure

)


        return a Dict[str, int] of {element: frequency} that shows the distribution of elements in BatchStructures.

        Parameters:
            count_for: 'Atom' or 'Structure', count element frequency by each atom in structures or each structure.
        

## extend

(

`batch_structures_list`: typing.Sequence

`strict`: <class 'bool'> = True

)


        Extend a list of BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures_list: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## generate_atom_list

(

`force_update`: <class 'bool'> = False

)


        Generate an attribute self.Atom_list (List[str]) which is the atom lists in order of the atomic coordinates sequence.

        Parameters:
            force_update: bool. if False, Atom_list would not be updated when it's not None.
        

## generate_atomic_number_list

(

`force_update`: <class 'bool'> = False

)


        Generate attribute self.Atomic_number_list (List[int]) which is the atomic number lists in order of the sequence of atom coordinates.

        Parameters:
            force_update: bool. if False, Atomic_number_list would not be updated when it's not None.
        

## generate_dist_mat

(

`supercell_indices`: <class 'inspect._empty'> = [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00]]

)


        Parameters:
            supercell_indices: NDArray[n_supercell, 3], the indices of supercells that calculate distance.

        self.Dist_mat Format: List[Tensor[(n_prim_cells, n_atom, n_atom)]]
        

## load

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

`mode`: typing.Literal['w', 'a'] = w

)


        Load data from saved files.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.
            mode: the data load mode. 'W' for write or overwrite existing data from data in file; 'a' for appending data in file to existing data.

        Returns: None

        

## load_from_file

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

)


        The class method version for loading data from saved files.
        WARNING: It would overwrite the existing BatchStructure data. Use `self.load(..., mode='a')` to retain existing data.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.

        Returns: Self with loaded data.

        

## not_contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that Not contain all given elements at the same time.
        

## not_contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

`verbose`: <class 'int'> = 0

)


        Return a view of BatchStructures that Not contain any of given elements.
        

## read

(

`file_list`: <class 'inspect._empty'> = None

`n_core`: <class 'int'> = -1

`backend`: typing.Union[typing.Literal['loky', 'threading', 'multiprocessing'], str] = loky

)

None

## rearrange

(

`indices`: typing.List[int]

)


        Rearrange the order of samples by given indices.
        Args:
            indices: indices of sample orders.

        Returns: None

        

## remove

(

`key`: int | str | slice

)


        Remove the data of given `key` in-place.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: None

        

## remove_copy

(

`key`: int | str | slice

)


        Remove the data of given `key` in a copy of self and return. The original data is not affected.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: copy of

        

## revise

(

`index`: int | str

`rev_Sample_ids`: None | str = None

`rev_Cells`: None | numpy.ndarray = None

`rev_Elements`: typing.Optional[typing.List[str]] = None

`rev_Numbers`: typing.Optional[typing.List[int]] = None

`rev_Coords_type`: typing.Optional[typing.Literal['C', 'D']] = None

`rev_Coords`: None | numpy.ndarray = None

`rev_Fixed`: None | numpy.ndarray = None

`rev_Energies`: None | float = None

`rev_Forces`: None | numpy.ndarray = None

`rev_Labels`: typing.Any | None = None

)


        Revising data of given `index`. None is for not changing.
        Args:
            index:
            rev_Sample_ids:
            rev_Cells:
            rev_Elements:
            rev_Numbers:
            rev_Coords_type:
            rev_Coords:
            rev_Fixed:
            rev_Energies:
            rev_Forces:
            rev_Labels:

        

## save

(

`path`: <class 'str'>

`mode`: typing.Literal['w', 'a'] = w

)


        Saving this BatchStructures to a numpy memory-mapping file.
        Each attribute in BatchStructures will be saved in the numpy memmap file with the same name.
        Additionally, file 'head' will record the information which is data type & shape of all attributes, and record which attributes are `None`.

        Args:
            path: the saving directory.
            mode: if 'w', create or overwrite the existing file for reading and writing. If 'a', data will append to the existing file.

        Returns: None

        

## select_by_element_number

(

`element_number_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that element number between element_number_range.
        

## select_by_energies

(

`energy_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that Energies between energy_range.
        

## select_by_prop

(

`prop`: <class 'str'>

`prop_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that given properties of BatchStructures between prop_range.
        The given properties must be comparable.

        Args:
            prop: an attribute name of self e.g., "Number", "Energies"
            prop_range: Tuple[float, float], range of prop to select. It is a left closed right open interval.

        Returns:
            BatchStructures which is a view of self
        

## select_by_sample_id

(

`pattern`: <class 'str'>

)


        Return a view of BatchStructures in which sample id could match the given pattern.
        Regular expressions are supported.
        For non-string sample id, str(*) would be applied first to convert id into string.
        Args:
            pattern: the (regular expressions) pattern to match sample ids in self.

        Returns: BatchStructures

        

## set_Energies

(

`val`: typing.Union[typing.Sequence, typing.Dict]

)


        Set or reset self.Energies from input `val`.
        Args:
            val: the input values to set self.Energies
                if Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## set_Forces

(

`val`: typing.Union[typing.Sequence[numpy.ndarray], typing.Dict[str, numpy.ndarray]]

)


        Set or reset self.Forces from `val`.
        Args:
            val: the input values to set self.Forces
                if Dict, val: {sample_id: forces, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns:

        

## set_Labels

(

`val`: typing.Union[typing.Sequence, typing.Dict, numpy.ndarray]

)


        Set or reset self.Labels from input `val`.
        Args:
            val: the input values of self.Labels to set.
            If Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## show

(

`number`: int | slice

)


        Show the information of samples in given slice `number`.
        Args:
            number: the slice of samples to show.

        Returns: None.

        

## shuffle

(

`seed`: <class 'int'> = None

)


        Shuffle the samples with given random seed.
        Args:
            seed: random seed.

        Returns: None

        

## sort_split_by_natoms

(

`labels`: typing.Union[typing.Dict, typing.List, NoneType] = None

`split_ratio`: <class 'float'> = 0.2

`n_core`: <class 'int'> = 1

`verbose`: <class 'int'> = 0

)


        Rearrange samples with different atom number into List[np.array] that list of NDArrays with the same atom number.
        Only work in 'L' Mode.

        Parameters:
            labels: Dict[id, label]|List[label]|None, the labels of samples. If labels is a List, it must have the same order as self.Sample_ids. If None, labels would be set to self.Labels.
            split_ratio: float between 0 and 1, the ratio of validation set.
            n_core:
            verbose: control the verboseness of output

        Returns:
            training_batches, val_batches: List_1[List_2[NDArray]]. List_1 is of diff. n_atom cells, List_2 is of (Cell, Atomic_number_list, Atom_coords)
            training_labels, val_labels: List[NDArray]. List is of diff. n_atom cells, NDArray is label.
            training_args, val_args: List[NDArray]. List is of diff. n_atom cells, NDArray is the indices of samples in self.Samp_id.
        

## write2text

(

`output_path`: <class 'str'> = ./

`indices`: typing.Union[int, str, typing.List[int], typing.Tuple[int, int], NoneType] = None

`file_format`: typing.Literal['POSCAR', 'cif', 'xyz', 'xyz_forces'] = POSCAR

`file_name_list`: typing.Union[str, typing.Sequence[str], NoneType] = None

`n_core`: <class 'int'> = -1

)


        Write selected structures to text files in given format.
        Args:
            indices: the selection indices of `self`. If Tuple, structures between `indices[0]` and `indices[1]` will be selected.
            file_format: the format of written files.
                'POSCAR': vasp POSCAR format
                'cif': crystallographic information file
                'xyz': ext-xyz file that only contains atomic positions
                'xyz_forces': ext-xyz file that contains atomic positions and forces
            output_path: the directory of output file.
            file_name_list: the list of file names. If None, it would be set to `Sample_ids`.
            n_core: number of CPU cores to write in parallel. `-1` for all available CPU cores.

        Returns: None

        

## ExtXyz2Feat

(

`path`: <class 'str'>

`verbose`: <class 'int'> = 1

)


    Read extxyz file with multiple structures.
    

## append

(

`batch_structures`: <class 'inspect._empty'>

`strict`: <class 'bool'> = True

)


        Append information of another BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## cartesian2direct

(

)

 Convert Cartesian coordinates to Direct coordinates. Only work in 'L' Mode. 

## contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain all given elements.
        

## contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain any of given elements.
        

## contain_only_in

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that only contain given elements.
        

## direct2cartesian

(

)

 Convert Direct coordinates to Cartesian coordinates. Only work in 'L' Mode. 

## elem_distribution

(

`count_for`: typing.Literal['Atom', 'Structure'] = Structure

)


        return a Dict[str, int] of {element: frequency} that shows the distribution of elements in BatchStructures.

        Parameters:
            count_for: 'Atom' or 'Structure', count element frequency by each atom in structures or each structure.
        

## extend

(

`batch_structures_list`: typing.Sequence

`strict`: <class 'bool'> = True

)


        Extend a list of BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures_list: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## generate_atom_list

(

`force_update`: <class 'bool'> = False

)


        Generate an attribute self.Atom_list (List[str]) which is the atom lists in order of the atomic coordinates sequence.

        Parameters:
            force_update: bool. if False, Atom_list would not be updated when it's not None.
        

## generate_atomic_number_list

(

`force_update`: <class 'bool'> = False

)


        Generate attribute self.Atomic_number_list (List[int]) which is the atomic number lists in order of the sequence of atom coordinates.

        Parameters:
            force_update: bool. if False, Atomic_number_list would not be updated when it's not None.
        

## generate_dist_mat

(

`supercell_indices`: <class 'inspect._empty'> = [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00]]

)


        Parameters:
            supercell_indices: NDArray[n_supercell, 3], the indices of supercells that calculate distance.

        self.Dist_mat Format: List[Tensor[(n_prim_cells, n_atom, n_atom)]]
        

## load

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

`mode`: typing.Literal['w', 'a'] = w

)


        Load data from saved files.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.
            mode: the data load mode. 'W' for write or overwrite existing data from data in file; 'a' for appending data in file to existing data.

        Returns: None

        

## load_from_file

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

)


        The class method version for loading data from saved files.
        WARNING: It would overwrite the existing BatchStructure data. Use `self.load(..., mode='a')` to retain existing data.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.

        Returns: Self with loaded data.

        

## not_contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that Not contain all given elements at the same time.
        

## not_contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

`verbose`: <class 'int'> = 0

)


        Return a view of BatchStructures that Not contain any of given elements.
        

## read

(

`file_list`: <class 'inspect._empty'> = None

`n_core`: <class 'int'> = -1

`backend`: typing.Union[typing.Literal['loky', 'threading', 'multiprocessing'], str] = loky

`lattice_tag`: <class 'str'> = lattice

`energy_tag`: <class 'str'> = energy

`column_info_tag`: <class 'str'> = properties

`element_tag`: <class 'str'> = species

`coordinates_tag`: <class 'str'> = pos

`forces_tag`: str | None = forces

`fixed_atom_tag`: str | None = move_mask

)


        Read *.extxyz files to BatchStructures.
        Args:
            file_list: List[str], the list of files to read. Default for all files under given path.
            n_core: int, the number of CPU cores used in reading files. -1 for all cores.
            backend: backend of parallel reading in `joblib`.
            lattice_tag: key-words of lattice information in *.extxyz file, at each structure's 2nd line.
            energy_tag: key-words of structure's energy in *.extxyz file.
            column_info_tag: key-words of column content information in *.extxyz file. The column content has such format:
                             `content 1`:`data type 1`:`column occupied number 1`:`content 2`:`data type 2`:`column occupied number 2`: ...
                             detailed see https://wiki.fysik.dtu.dk/ase/dev/_modules/ase/io/extxyz.html.
            element_tag: As a content in `column_info_tag`, name of element column.
            coordinates_tag: As a content in `column_info_tag`, name of atom coordinates column.
            forces_tag: As a content in `column_info_tag`, name of forces column. If the file does not contain forces, set it to None.
            fixed_atom_tag: As a content in `column_info_tag`, name of the mask column specified which atom was fixed.

        Returns: None
        All data would update as class attributes.
        

## rearrange

(

`indices`: typing.List[int]

)


        Rearrange the order of samples by given indices.
        Args:
            indices: indices of sample orders.

        Returns: None

        

## remove

(

`key`: int | str | slice

)


        Remove the data of given `key` in-place.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: None

        

## remove_copy

(

`key`: int | str | slice

)


        Remove the data of given `key` in a copy of self and return. The original data is not affected.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: copy of

        

## revise

(

`index`: int | str

`rev_Sample_ids`: None | str = None

`rev_Cells`: None | numpy.ndarray = None

`rev_Elements`: typing.Optional[typing.List[str]] = None

`rev_Numbers`: typing.Optional[typing.List[int]] = None

`rev_Coords_type`: typing.Optional[typing.Literal['C', 'D']] = None

`rev_Coords`: None | numpy.ndarray = None

`rev_Fixed`: None | numpy.ndarray = None

`rev_Energies`: None | float = None

`rev_Forces`: None | numpy.ndarray = None

`rev_Labels`: typing.Any | None = None

)


        Revising data of given `index`. None is for not changing.
        Args:
            index:
            rev_Sample_ids:
            rev_Cells:
            rev_Elements:
            rev_Numbers:
            rev_Coords_type:
            rev_Coords:
            rev_Fixed:
            rev_Energies:
            rev_Forces:
            rev_Labels:

        

## save

(

`path`: <class 'str'>

`mode`: typing.Literal['w', 'a'] = w

)


        Saving this BatchStructures to a numpy memory-mapping file.
        Each attribute in BatchStructures will be saved in the numpy memmap file with the same name.
        Additionally, file 'head' will record the information which is data type & shape of all attributes, and record which attributes are `None`.

        Args:
            path: the saving directory.
            mode: if 'w', create or overwrite the existing file for reading and writing. If 'a', data will append to the existing file.

        Returns: None

        

## select_by_element_number

(

`element_number_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that element number between element_number_range.
        

## select_by_energies

(

`energy_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that Energies between energy_range.
        

## select_by_prop

(

`prop`: <class 'str'>

`prop_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that given properties of BatchStructures between prop_range.
        The given properties must be comparable.

        Args:
            prop: an attribute name of self e.g., "Number", "Energies"
            prop_range: Tuple[float, float], range of prop to select. It is a left closed right open interval.

        Returns:
            BatchStructures which is a view of self
        

## select_by_sample_id

(

`pattern`: <class 'str'>

)


        Return a view of BatchStructures in which sample id could match the given pattern.
        Regular expressions are supported.
        For non-string sample id, str(*) would be applied first to convert id into string.
        Args:
            pattern: the (regular expressions) pattern to match sample ids in self.

        Returns: BatchStructures

        

## set_Energies

(

`val`: typing.Union[typing.Sequence, typing.Dict]

)


        Set or reset self.Energies from input `val`.
        Args:
            val: the input values to set self.Energies
                if Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## set_Forces

(

`val`: typing.Union[typing.Sequence[numpy.ndarray], typing.Dict[str, numpy.ndarray]]

)


        Set or reset self.Forces from `val`.
        Args:
            val: the input values to set self.Forces
                if Dict, val: {sample_id: forces, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns:

        

## set_Labels

(

`val`: typing.Union[typing.Sequence, typing.Dict, numpy.ndarray]

)


        Set or reset self.Labels from input `val`.
        Args:
            val: the input values of self.Labels to set.
            If Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## show

(

`number`: int | slice

)


        Show the information of samples in given slice `number`.
        Args:
            number: the slice of samples to show.

        Returns: None.

        

## shuffle

(

`seed`: <class 'int'> = None

)


        Shuffle the samples with given random seed.
        Args:
            seed: random seed.

        Returns: None

        

## sort_split_by_natoms

(

`labels`: typing.Union[typing.Dict, typing.List, NoneType] = None

`split_ratio`: <class 'float'> = 0.2

`n_core`: <class 'int'> = 1

`verbose`: <class 'int'> = 0

)


        Rearrange samples with different atom number into List[np.array] that list of NDArrays with the same atom number.
        Only work in 'L' Mode.

        Parameters:
            labels: Dict[id, label]|List[label]|None, the labels of samples. If labels is a List, it must have the same order as self.Sample_ids. If None, labels would be set to self.Labels.
            split_ratio: float between 0 and 1, the ratio of validation set.
            n_core:
            verbose: control the verboseness of output

        Returns:
            training_batches, val_batches: List_1[List_2[NDArray]]. List_1 is of diff. n_atom cells, List_2 is of (Cell, Atomic_number_list, Atom_coords)
            training_labels, val_labels: List[NDArray]. List is of diff. n_atom cells, NDArray is label.
            training_args, val_args: List[NDArray]. List is of diff. n_atom cells, NDArray is the indices of samples in self.Samp_id.
        

## write2text

(

`output_path`: <class 'str'> = ./

`indices`: typing.Union[int, str, typing.List[int], typing.Tuple[int, int], NoneType] = None

`file_format`: typing.Literal['POSCAR', 'cif', 'xyz', 'xyz_forces'] = POSCAR

`file_name_list`: typing.Union[str, typing.Sequence[str], NoneType] = None

`n_core`: <class 'int'> = -1

)


        Write selected structures to text files in given format.
        Args:
            indices: the selection indices of `self`. If Tuple, structures between `indices[0]` and `indices[1]` will be selected.
            file_format: the format of written files.
                'POSCAR': vasp POSCAR format
                'cif': crystallographic information file
                'xyz': ext-xyz file that only contains atomic positions
                'xyz_forces': ext-xyz file that contains atomic positions and forces
            output_path: the directory of output file.
            file_name_list: the list of file names. If None, it would be set to `Sample_ids`.
            n_core: number of CPU cores to write in parallel. `-1` for all available CPU cores.

        Returns: None

        

## load_from_csv

(

`file_name`: <class 'str'>

`label_type`: <class 'type'> = <class 'float'>

`ignore_None_label_samp`: <class 'bool'> = True

`read_column`: typing.Tuple[int, int] = (0, 1)

`has_title_line`: <class 'bool'> = False

)


    load information of a csv file into a dict of {samp_1:label_1, ...}.

    Parameters:
        file_name: str, csv file of 2 columns (sample name, sample label)
        label_type: type, type of sample label
        ignore_None_label_samp: bool, whether ignore None label samples i.e., not put them into output dict
        read_column: Tuple[int,int], the 2 columns to read, where the 1st column as keys and the 2nd as values.
        has_title_line: bool, whether ignore the 1st line which is the title or descriptions.

    Return:
        dict of {samp_1:label_1, ...} | dict, id_list of [samp_names]
    

## Cif2Feat

(

`path`: <class 'str'>

`verbose`: <class 'int'> = 1

)


    Read CIF file with multiple structures.
    Notes: CIF file could not contain the fixation information, so all atoms would be free.

    

## append

(

`batch_structures`: <class 'inspect._empty'>

`strict`: <class 'bool'> = True

)


        Append information of another BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## cartesian2direct

(

)

 Convert Cartesian coordinates to Direct coordinates. Only work in 'L' Mode. 

## contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain all given elements.
        

## contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain any of given elements.
        

## contain_only_in

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that only contain given elements.
        

## direct2cartesian

(

)

 Convert Direct coordinates to Cartesian coordinates. Only work in 'L' Mode. 

## elem_distribution

(

`count_for`: typing.Literal['Atom', 'Structure'] = Structure

)


        return a Dict[str, int] of {element: frequency} that shows the distribution of elements in BatchStructures.

        Parameters:
            count_for: 'Atom' or 'Structure', count element frequency by each atom in structures or each structure.
        

## extend

(

`batch_structures_list`: typing.Sequence

`strict`: <class 'bool'> = True

)


        Extend a list of BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures_list: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## generate_atom_list

(

`force_update`: <class 'bool'> = False

)


        Generate an attribute self.Atom_list (List[str]) which is the atom lists in order of the atomic coordinates sequence.

        Parameters:
            force_update: bool. if False, Atom_list would not be updated when it's not None.
        

## generate_atomic_number_list

(

`force_update`: <class 'bool'> = False

)


        Generate attribute self.Atomic_number_list (List[int]) which is the atomic number lists in order of the sequence of atom coordinates.

        Parameters:
            force_update: bool. if False, Atomic_number_list would not be updated when it's not None.
        

## generate_dist_mat

(

`supercell_indices`: <class 'inspect._empty'> = [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00]]

)


        Parameters:
            supercell_indices: NDArray[n_supercell, 3], the indices of supercells that calculate distance.

        self.Dist_mat Format: List[Tensor[(n_prim_cells, n_atom, n_atom)]]
        

## load

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

`mode`: typing.Literal['w', 'a'] = w

)


        Load data from saved files.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.
            mode: the data load mode. 'W' for write or overwrite existing data from data in file; 'a' for appending data in file to existing data.

        Returns: None

        

## load_from_file

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

)


        The class method version for loading data from saved files.
        WARNING: It would overwrite the existing BatchStructure data. Use `self.load(..., mode='a')` to retain existing data.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.

        Returns: Self with loaded data.

        

## not_contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that Not contain all given elements at the same time.
        

## not_contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

`verbose`: <class 'int'> = 0

)


        Return a view of BatchStructures that Not contain any of given elements.
        

## read

(

`file_list`: <class 'inspect._empty'> = None

`n_core`: <class 'int'> = -1

`backend`: typing.Union[typing.Literal['loky', 'threading', 'multiprocessing'], str] = loky

)

None

## rearrange

(

`indices`: typing.List[int]

)


        Rearrange the order of samples by given indices.
        Args:
            indices: indices of sample orders.

        Returns: None

        

## remove

(

`key`: int | str | slice

)


        Remove the data of given `key` in-place.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: None

        

## remove_copy

(

`key`: int | str | slice

)


        Remove the data of given `key` in a copy of self and return. The original data is not affected.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: copy of

        

## revise

(

`index`: int | str

`rev_Sample_ids`: None | str = None

`rev_Cells`: None | numpy.ndarray = None

`rev_Elements`: typing.Optional[typing.List[str]] = None

`rev_Numbers`: typing.Optional[typing.List[int]] = None

`rev_Coords_type`: typing.Optional[typing.Literal['C', 'D']] = None

`rev_Coords`: None | numpy.ndarray = None

`rev_Fixed`: None | numpy.ndarray = None

`rev_Energies`: None | float = None

`rev_Forces`: None | numpy.ndarray = None

`rev_Labels`: typing.Any | None = None

)


        Revising data of given `index`. None is for not changing.
        Args:
            index:
            rev_Sample_ids:
            rev_Cells:
            rev_Elements:
            rev_Numbers:
            rev_Coords_type:
            rev_Coords:
            rev_Fixed:
            rev_Energies:
            rev_Forces:
            rev_Labels:

        

## save

(

`path`: <class 'str'>

`mode`: typing.Literal['w', 'a'] = w

)


        Saving this BatchStructures to a numpy memory-mapping file.
        Each attribute in BatchStructures will be saved in the numpy memmap file with the same name.
        Additionally, file 'head' will record the information which is data type & shape of all attributes, and record which attributes are `None`.

        Args:
            path: the saving directory.
            mode: if 'w', create or overwrite the existing file for reading and writing. If 'a', data will append to the existing file.

        Returns: None

        

## select_by_element_number

(

`element_number_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that element number between element_number_range.
        

## select_by_energies

(

`energy_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that Energies between energy_range.
        

## select_by_prop

(

`prop`: <class 'str'>

`prop_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that given properties of BatchStructures between prop_range.
        The given properties must be comparable.

        Args:
            prop: an attribute name of self e.g., "Number", "Energies"
            prop_range: Tuple[float, float], range of prop to select. It is a left closed right open interval.

        Returns:
            BatchStructures which is a view of self
        

## select_by_sample_id

(

`pattern`: <class 'str'>

)


        Return a view of BatchStructures in which sample id could match the given pattern.
        Regular expressions are supported.
        For non-string sample id, str(*) would be applied first to convert id into string.
        Args:
            pattern: the (regular expressions) pattern to match sample ids in self.

        Returns: BatchStructures

        

## set_Energies

(

`val`: typing.Union[typing.Sequence, typing.Dict]

)


        Set or reset self.Energies from input `val`.
        Args:
            val: the input values to set self.Energies
                if Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## set_Forces

(

`val`: typing.Union[typing.Sequence[numpy.ndarray], typing.Dict[str, numpy.ndarray]]

)


        Set or reset self.Forces from `val`.
        Args:
            val: the input values to set self.Forces
                if Dict, val: {sample_id: forces, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns:

        

## set_Labels

(

`val`: typing.Union[typing.Sequence, typing.Dict, numpy.ndarray]

)


        Set or reset self.Labels from input `val`.
        Args:
            val: the input values of self.Labels to set.
            If Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## show

(

`number`: int | slice

)


        Show the information of samples in given slice `number`.
        Args:
            number: the slice of samples to show.

        Returns: None.

        

## shuffle

(

`seed`: <class 'int'> = None

)


        Shuffle the samples with given random seed.
        Args:
            seed: random seed.

        Returns: None

        

## sort_split_by_natoms

(

`labels`: typing.Union[typing.Dict, typing.List, NoneType] = None

`split_ratio`: <class 'float'> = 0.2

`n_core`: <class 'int'> = 1

`verbose`: <class 'int'> = 0

)


        Rearrange samples with different atom number into List[np.array] that list of NDArrays with the same atom number.
        Only work in 'L' Mode.

        Parameters:
            labels: Dict[id, label]|List[label]|None, the labels of samples. If labels is a List, it must have the same order as self.Sample_ids. If None, labels would be set to self.Labels.
            split_ratio: float between 0 and 1, the ratio of validation set.
            n_core:
            verbose: control the verboseness of output

        Returns:
            training_batches, val_batches: List_1[List_2[NDArray]]. List_1 is of diff. n_atom cells, List_2 is of (Cell, Atomic_number_list, Atom_coords)
            training_labels, val_labels: List[NDArray]. List is of diff. n_atom cells, NDArray is label.
            training_args, val_args: List[NDArray]. List is of diff. n_atom cells, NDArray is the indices of samples in self.Samp_id.
        

## write2text

(

`output_path`: <class 'str'> = ./

`indices`: typing.Union[int, str, typing.List[int], typing.Tuple[int, int], NoneType] = None

`file_format`: typing.Literal['POSCAR', 'cif', 'xyz', 'xyz_forces'] = POSCAR

`file_name_list`: typing.Union[str, typing.Sequence[str], NoneType] = None

`n_core`: <class 'int'> = -1

)


        Write selected structures to text files in given format.
        Args:
            indices: the selection indices of `self`. If Tuple, structures between `indices[0]` and `indices[1]` will be selected.
            file_format: the format of written files.
                'POSCAR': vasp POSCAR format
                'cif': crystallographic information file
                'xyz': ext-xyz file that only contains atomic positions
                'xyz_forces': ext-xyz file that contains atomic positions and forces
            output_path: the directory of output file.
            file_name_list: the list of file names. If None, it would be set to `Sample_ids`.
            n_core: number of CPU cores to write in parallel. `-1` for all available CPU cores.

        Returns: None

        

## load_from_structures

(

`path`: <class 'str'>

)


    Load BatchStructure memory-mapping files from `path` and return this BatchStructures.
    Args:
        path: the path of BatchStructure memory-mapping files.

    Returns: BatchStructures with read data.

    

## Output2Feat

(

`path`: <class 'str'>

`verbose`: <class 'int'> = 1

)


    A class of post-processing to reading output files of BatchOptimization and BatchMD
    

## append

(

`batch_structures`: <class 'inspect._empty'>

`strict`: <class 'bool'> = True

)


        Append information of another BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## cartesian2direct

(

)

 Convert Cartesian coordinates to Direct coordinates. Only work in 'L' Mode. 

## contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain all given elements.
        

## contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that contain any of given elements.
        

## contain_only_in

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that only contain given elements.
        

## direct2cartesian

(

)

 Convert Direct coordinates to Cartesian coordinates. Only work in 'L' Mode. 

## elem_distribution

(

`count_for`: typing.Literal['Atom', 'Structure'] = Structure

)


        return a Dict[str, int] of {element: frequency} that shows the distribution of elements in BatchStructures.

        Parameters:
            count_for: 'Atom' or 'Structure', count element frequency by each atom in structures or each structure.
        

## extend

(

`batch_structures_list`: typing.Sequence

`strict`: <class 'bool'> = True

)


        Extend a list of BatchStructures to self.
        If original data do not have some properties but appending data do,
         these properties of original data would be padded with `None`, and vice versa.
        Args:
            batch_structures_list: the BatchStructures to append
            strict: If True, `batch_structures` contains any id which is already in `self` would raise an Error;
                    otherwise, the data will be overwritten if encountered the same id.

        Returns: None

        

## generate_atom_list

(

`force_update`: <class 'bool'> = False

)


        Generate an attribute self.Atom_list (List[str]) which is the atom lists in order of the atomic coordinates sequence.

        Parameters:
            force_update: bool. if False, Atom_list would not be updated when it's not None.
        

## generate_atomic_number_list

(

`force_update`: <class 'bool'> = False

)


        Generate attribute self.Atomic_number_list (List[int]) which is the atomic number lists in order of the sequence of atom coordinates.

        Parameters:
            force_update: bool. if False, Atomic_number_list would not be updated when it's not None.
        

## generate_dist_mat

(

`supercell_indices`: <class 'inspect._empty'> = [[ 0.00000000e+00  0.00000000e+00  0.00000000e+00]]

)


        Parameters:
            supercell_indices: NDArray[n_supercell, 3], the indices of supercells that calculate distance.

        self.Dist_mat Format: List[Tensor[(n_prim_cells, n_atom, n_atom)]]
        

## load

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

`mode`: typing.Literal['w', 'a'] = w

)


        Load data from saved files.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.
            mode: the data load mode. 'W' for write or overwrite existing data from data in file; 'a' for appending data in file to existing data.

        Returns: None

        

## load_from_file

(

`path`: <class 'str'>

`data_slice`: typing.Optional[typing.Tuple[int, int]] = None

)


        The class method version for loading data from saved files.
        WARNING: It would overwrite the existing BatchStructure data. Use `self.load(..., mode='a')` to retain existing data.
        Args:
            path: the file path.
            data_slice: The piece of data in files to be read. If None, all data in files would be read into memory.

        Returns: Self with loaded data.

        

## not_contain_all

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

)


        Return a view of BatchStructures that Not contain all given elements at the same time.
        

## not_contain_any

(

`elements`: typing.Union[typing.List[str], typing.Set[str]]

`verbose`: <class 'int'> = 0

)


        Return a view of BatchStructures that Not contain any of given elements.
        

## read

(

`file_list`: typing.List[str]

`n_core`: <class 'int'> = -1

`backend`: <class 'inspect._empty'> = loky

)

None

## rearrange

(

`indices`: typing.List[int]

)


        Rearrange the order of samples by given indices.
        Args:
            indices: indices of sample orders.

        Returns: None

        

## remove

(

`key`: int | str | slice

)


        Remove the data of given `key` in-place.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: None

        

## remove_copy

(

`key`: int | str | slice

)


        Remove the data of given `key` in a copy of self and return. The original data is not affected.
        Args:
            key: int for index, str for Sample_ids, slice for a slice of indices.

        Returns: copy of

        

## revise

(

`index`: int | str

`rev_Sample_ids`: None | str = None

`rev_Cells`: None | numpy.ndarray = None

`rev_Elements`: typing.Optional[typing.List[str]] = None

`rev_Numbers`: typing.Optional[typing.List[int]] = None

`rev_Coords_type`: typing.Optional[typing.Literal['C', 'D']] = None

`rev_Coords`: None | numpy.ndarray = None

`rev_Fixed`: None | numpy.ndarray = None

`rev_Energies`: None | float = None

`rev_Forces`: None | numpy.ndarray = None

`rev_Labels`: typing.Any | None = None

)


        Revising data of given `index`. None is for not changing.
        Args:
            index:
            rev_Sample_ids:
            rev_Cells:
            rev_Elements:
            rev_Numbers:
            rev_Coords_type:
            rev_Coords:
            rev_Fixed:
            rev_Energies:
            rev_Forces:
            rev_Labels:

        

## save

(

`path`: <class 'str'>

`mode`: typing.Literal['w', 'a'] = w

)


        Saving this BatchStructures to a numpy memory-mapping file.
        Each attribute in BatchStructures will be saved in the numpy memmap file with the same name.
        Additionally, file 'head' will record the information which is data type & shape of all attributes, and record which attributes are `None`.

        Args:
            path: the saving directory.
            mode: if 'w', create or overwrite the existing file for reading and writing. If 'a', data will append to the existing file.

        Returns: None

        

## select_by_element_number

(

`element_number_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that element number between element_number_range.
        

## select_by_energies

(

`energy_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that Energies between energy_range.
        

## select_by_prop

(

`prop`: <class 'str'>

`prop_range`: typing.Tuple[float, float]

)


        Return a view of BatchStructures that given properties of BatchStructures between prop_range.
        The given properties must be comparable.

        Args:
            prop: an attribute name of self e.g., "Number", "Energies"
            prop_range: Tuple[float, float], range of prop to select. It is a left closed right open interval.

        Returns:
            BatchStructures which is a view of self
        

## select_by_sample_id

(

`pattern`: <class 'str'>

)


        Return a view of BatchStructures in which sample id could match the given pattern.
        Regular expressions are supported.
        For non-string sample id, str(*) would be applied first to convert id into string.
        Args:
            pattern: the (regular expressions) pattern to match sample ids in self.

        Returns: BatchStructures

        

## set_Energies

(

`val`: typing.Union[typing.Sequence, typing.Dict]

)


        Set or reset self.Energies from input `val`.
        Args:
            val: the input values to set self.Energies
                if Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## set_Forces

(

`val`: typing.Union[typing.Sequence[numpy.ndarray], typing.Dict[str, numpy.ndarray]]

)


        Set or reset self.Forces from `val`.
        Args:
            val: the input values to set self.Forces
                if Dict, val: {sample_id: forces, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns:

        

## set_Labels

(

`val`: typing.Union[typing.Sequence, typing.Dict, numpy.ndarray]

)


        Set or reset self.Labels from input `val`.
        Args:
            val: the input values of self.Labels to set.
            If Dict, val: {sample_id: energy, ...}; if Sequence, it must have the same order of self.Sample_ids.

        Returns: None

        

## show

(

`number`: int | slice

)


        Show the information of samples in given slice `number`.
        Args:
            number: the slice of samples to show.

        Returns: None.

        

## shuffle

(

`seed`: <class 'int'> = None

)


        Shuffle the samples with given random seed.
        Args:
            seed: random seed.

        Returns: None

        

## sort_split_by_natoms

(

`labels`: typing.Union[typing.Dict, typing.List, NoneType] = None

`split_ratio`: <class 'float'> = 0.2

`n_core`: <class 'int'> = 1

`verbose`: <class 'int'> = 0

)


        Rearrange samples with different atom number into List[np.array] that list of NDArrays with the same atom number.
        Only work in 'L' Mode.

        Parameters:
            labels: Dict[id, label]|List[label]|None, the labels of samples. If labels is a List, it must have the same order as self.Sample_ids. If None, labels would be set to self.Labels.
            split_ratio: float between 0 and 1, the ratio of validation set.
            n_core:
            verbose: control the verboseness of output

        Returns:
            training_batches, val_batches: List_1[List_2[NDArray]]. List_1 is of diff. n_atom cells, List_2 is of (Cell, Atomic_number_list, Atom_coords)
            training_labels, val_labels: List[NDArray]. List is of diff. n_atom cells, NDArray is label.
            training_args, val_args: List[NDArray]. List is of diff. n_atom cells, NDArray is the indices of samples in self.Samp_id.
        

## write2text

(

`output_path`: <class 'str'> = ./

`indices`: typing.Union[int, str, typing.List[int], typing.Tuple[int, int], NoneType] = None

`file_format`: typing.Literal['POSCAR', 'cif', 'xyz', 'xyz_forces'] = POSCAR

`file_name_list`: typing.Union[str, typing.Sequence[str], NoneType] = None

`n_core`: <class 'int'> = -1

)


        Write selected structures to text files in given format.
        Args:
            indices: the selection indices of `self`. If Tuple, structures between `indices[0]` and `indices[1]` will be selected.
            file_format: the format of written files.
                'POSCAR': vasp POSCAR format
                'cif': crystallographic information file
                'xyz': ext-xyz file that only contains atomic positions
                'xyz_forces': ext-xyz file that contains atomic positions and forces
            output_path: the directory of output file.
            file_name_list: the list of file names. If None, it would be set to `Sample_ids`.
            n_core: number of CPU cores to write in parallel. `-1` for all available CPU cores.

        Returns: None

        

